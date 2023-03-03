from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name + " / " + self.email + " / " + self.message




class About(models.Model):
    

    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    emid = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " | " + "  " + self.number + " | " + "  " + self.address + " | " + "  " + self.role + " | " + self.emid
    


