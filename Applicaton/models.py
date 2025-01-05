from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name=models.CharField(max_length=60)
    objective=models.TextField()
    dob=models.DateField()
    place=models.CharField(max_length=100)
    email=models.CharField(max_length=60)
    contact=models.IntegerField()
    img=models.ImageField()
    img2 = models.ImageField(default='default_image_path.jpg')
 
    def __str__(self):
        return self.name

class GraductionEducation(models.Model):
    institiute=models.CharField(max_length=100)
    cls=models.CharField(max_length=100)
    course=models.CharField(max_length=60)
    place = models.CharField(max_length=255, default='Unknown')

    def __str__(self) -> str:
        return self.cls

class SchoolEducation(models.Model):
    institiute=models.CharField(max_length=100)
    cls=models.CharField(max_length=100)
    course=models.CharField(max_length=60)
    place = models.CharField(max_length=255, default='Unknown')
    

    def __str__(self) -> str:
        return self.cls       
    
    
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10,default="phone")
    description=models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    Pimg=models.ImageField()
    Pname=models.CharField(max_length= 50)
    Pdis=models.TextField()
    plink=models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.Pname


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


class Hobbie(models.Model):
    name = models.CharField(max_length=100, verbose_name="hobbies")
    image = models.ImageField(upload_to="hobbie")

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title

class Skil(models.Model):
    title = models.CharField(max_length=100, verbose_name="sklis")
    image = models.ImageField(upload_to="skils")

    def __str__(self):
        return self.title