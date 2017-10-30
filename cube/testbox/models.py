from django.db import models

# Create your models here.
class chat_log(models.Model):
    # to store the chat of the user
    source = models.TextField(max_length=20)
    chat = models.TextField(max_length=500)


    # this returns the chart  of the  printed
    def __chat_log__(self):
        return self
        #return self.source