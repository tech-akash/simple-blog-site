
from distutils import core
from django.db import models
from django.urls import reverse
from froala_editor.fields import FroalaField

# this is model of blog 
class blogModel(models.Model):
    blog_title=models.CharField(max_length=200)
    blogContent=FroalaField()
    blog_image=models.ImageField(upload_to='images',null=True,blank=True)
    timeStamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.blog_title
    # function when called return absoulte url of that object
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    