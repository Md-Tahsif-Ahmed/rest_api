from django.db import models

 





def upload_path(instance, filname):
    return '/'.join(['images', str(instance.title), filname])
 
class Category(models.Model):
    title = models.CharField(max_length=32, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
     
     
     

 


 