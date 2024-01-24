from django.db import models


# Qurulishlar uchun
class Construction(models.Model):
    image = models.ImageField(upload_to='items/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Bosh sahifadagi Loyixalar uchun
class Project(models.Model):
    image = models.ImageField(upload_to='items/')
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Loyixalar sahihasi uchun
class ListProject(models.Model):
    image = models.ImageField(upload_to='items/')
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Blog qisim uchun
class Blog(models.Model):
    image = models.ImageField(upload_to='items/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Bog`lanish uchun
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.TextField()
    message = models.TextField()
    is_checked = models.BooleanField(default=False)
