from django.db import models
import os
# Create your models here.

class BookStoreModel(models.Model):
    CATEGORY=(
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi','Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror')
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30,choices=CATEGORY)
    pdf = models.FileField(upload_to='books/pdfs',null=True,blank=True)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.book_name
    
    # for delete pdf
    def delete(self, *args, **kwargs):
        if self.pdf:
            if os.path.isfile(self.pdf.path):
                os.remove(self.pdf.path)
        super(BookStoreModel, self).delete(*args, **kwargs)