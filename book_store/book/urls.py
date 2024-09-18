from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from book import views
urlpatterns = [
    path('',views.home.as_view(), name='home'),
    path("book_detail/<int:id>", views.BookDetails.as_view(), name="book_detail"), # template view url
    path('book_details/<int:id>', views.BookDetailsView.as_view(), name= 'book_details'),  # detailsView urls
    path('store_new_book/',views.store_book, name='store_book'),
    # path('show_books/',views.show_books, name='show_book'),
    path('show_books/', views.BookListView.as_view(), name = 'show_book'),
    path('view_pdf/<int:pk>/', views.view_pdf, name='view_pdf'),
    path('edit_book/<int:id>/',views.edit_book,name='edit_book'),
    path('delete_book/<int:id>/',views.delete_book,name='delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)