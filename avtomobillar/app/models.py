from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    category = models.ForeignKey(Brand, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    published = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name