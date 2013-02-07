from django.db import models

from mezzanine.blog.models import BlogPost
import filebrowser_safe
from filebrowser_safe.fields import FileBrowseField

# Create your models here.

Post_Libation_Choices = (
    (u'B', u'Beer'),
    (u'W', u'Wine'),
    (u'L', u'Liqor'),
    (u'S', u'Smoothie'),
    (u'J', u'Juice'),
    (u'T', u'Tea'),
    (u'E', u'Espresso'),
    (u'C', u'Cultured Drink'),
)

class PostWithLibation(BlogPost):
     post_libation_title = models.CharField(max_length = 30)
     post_libation_type_choice = models.CharField(max_length = 20, choices=Post_Libation_Choices)
     post_libation_recipe = models.TextField()
     post_libation_image = filebrowser_safe.fields.FileBrowseField("Image", max_length = 200, directory = "drink_images/", extensions = ".png", blank=True, null=True)

#class imageforlibation(secondlibation):
#    typeimage = OneToOneField(secondlibation,)
