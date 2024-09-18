from django.contrib import admin
from book.models import BookStoreModel
# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','author','category','first_pub','last_pub')
    search_fields = ('book_name', 'author')
    list_filter = ('first_pub', 'author','category')
admin.site.register(BookStoreModel,BookStoreModelAdmin)