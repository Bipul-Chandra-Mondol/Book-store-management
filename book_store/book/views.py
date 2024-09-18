from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView,DetailView
import os
# Create your views here.
# function based view
# def home(request):
#     return render(request,'home.html')

# class based vied
class home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        book = BookStoreModel.objects.all()
        context['book'] = book
        # context.update(kwargs) # update dictionary with url parameter(comes from url)
        return context

# class based view -> Template view  
class BookDetails(TemplateView):
    template_name = 'book_details.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        book = BookStoreModel.objects.get(id = kwargs['id'])
        context = {'book':book}
        return context
# avobe function and this are same work (diffrent in views)
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'

def store_book(request):
    if request.method == 'POST':
        book=BookStoreForm(request.POST, request.FILES)
        if book.is_valid():
            print(book.cleaned_data)
            book.save(commit=True)
            return redirect('show_books')
    else:
        book = BookStoreForm()
    
    return render(request,'store_book.html',{'form':book})

'''
def show_books(request):
    book = BookStoreModel.objects.all()
    return render(request,'show_book.html',{'data':book})
'''
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html' 
    context_object_name = 'booklist'
    '''def get_queryset(self):
        return BookStoreModel.objects.filter(author = 'Rabindra Nath Tagore') '''
    '''def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'booklist':BookStoreModel.objects.all().order_by('author')
        }
        return context '''
    ordering = ['-id']
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = 'staff.html'
        else:
            template_name = self.template_name
        return [template_name]
    
def view_pdf(request, pk):
    book = get_object_or_404(BookStoreModel, pk=pk)
    response = HttpResponse(book.pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{book.pdf.name}"'
    return response

def edit_book(request,id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        # Check if a new file is being uploaded
        if 'pdf' in request.FILES:
            # Delete the old file if it exists
            if book.pdf and os.path.isfile(book.pdf.path):
                os.remove(book.pdf.path)
        form = BookStoreForm(request.POST, request.FILES, instance=book)
        if form.is_valid:
            form.save(commit=True)
            return redirect('show_books')
    return render(request,'store_book.html',{'form':form})

def delete_book(request,id):
    book = get_object_or_404(BookStoreModel, pk = id)
    book.delete()
    return redirect('show_books')
    