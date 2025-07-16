from django.db import models

class knpwledge(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField(max_length=255)
    


    
