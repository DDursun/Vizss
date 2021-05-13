from django.db import models

# Creating models
class Customer(models.Model):
    name = models.CharField(max_length=120)
    log = models.ImageField(upload_to = 'customers', default = 'nopicture.png')
    def __str__(self):
        return str(self.name)