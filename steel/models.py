from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.



class Page(models.Model):
	Title=models.CharField(max_length=350)
	Description=models.TextField()
	image=models.ImageField(upload_to='Ndonga_photo/',blank=False,null=True) 
	#image_url = models.URLField()
	created_on=models.DateTimeField(auto_now_add=True)




class SteelType(models.Model):
    name = models.CharField(max_length=200)
    image=models.ImageField(upload_to='Ndonga_photo/',blank=False,null=False) 
    description = models.TextField()


class Quotation(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    steel_type = models.ForeignKey(SteelType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    additional_comments = models.TextField()




class About(models.Model):
	Description=models.TextField()
	Photo=models.ImageField(upload_to='About_photo/',blank=False,null=False)



    




	