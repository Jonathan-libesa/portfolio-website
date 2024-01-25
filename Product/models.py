from django.db import models

# Create your models here.


class Door(models.Model):
    image=models.ImageField(upload_to='Ndonga_photo/',blank=False,null=False) 


class Window(models.Model):
    image=models.ImageField(upload_to='Ndonga_photo/',blank=False,null=False)


class Gate(models.Model):
    image=models.ImageField(upload_to='Ndonga_photo/',blank=False,null=False)



class Quotation(models.Model):
    door = models.ForeignKey('Door', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_Phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.door}"



class Quotation1(models.Model):
    window = models.ForeignKey('Window', on_delete=models.CASCADE)  # Corrected from ' Window' to 'Window'
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_Phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.window}"



class Quotation2(models.Model):
   
    gate = models.ForeignKey('Gate', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_Phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.gate}"