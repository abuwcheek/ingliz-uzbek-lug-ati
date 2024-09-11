from django.db import models
from django.utils.text import slugify
from PIL import Image
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True


class Category(BaseModel):
     title = models.CharField(max_length=255)
     slug = models.SlugField()
     image = models.ImageField(upload_to='category_images/')


     def __str__(self):
          return self.title


     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug=slugify(self.title, allow_unicode=True)
          return super().save(*args, **kwargs)
     

class Word(BaseModel):
     category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category_word", null=True)
     en_form = models.CharField(max_length=50)
     slug = models.SlugField()
     uz_form = models.CharField(max_length=200)
     en_definition = RichTextField()
     uz_definition = RichTextField()
     image = models.ImageField(upload_to='images/')

     def __str__(self):
          return f'{self.en_form} - {self.uz_form}'


     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug=slugify(self.en_form, allow_unicode=True)
          return super().save(*args, **kwargs)



class About(BaseModel):
     locatin = models.CharField(max_length=50)
     phone = models.CharField(max_length=15)
     email = models.EmailField()

     instagram = models.CharField(max_length=100)
     facebook = models.CharField(max_length=100)
     youtube = models.CharField(max_length=100)
     twitter = models.CharField(max_length=100)
     linkedin = models.CharField(max_length=100)

     image = models.ImageField(upload_to="about_images/")
     body = models.TextField()


     def __str__(self):
          return "About"



class Contact(BaseModel):
     name = models.CharField(max_length=100)
     number = models.CharField(max_length=15)
     email = models.EmailField()
     message = models.CharField(max_length=100)

     
     def __str__(self):
          return "Contact"