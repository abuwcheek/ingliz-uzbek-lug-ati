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

     

class Word(BaseModel):
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
