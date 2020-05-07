from django.db import models
#makemigration---create changes and store into files
#migrate---apply the pending changes created by makemigrations
#creating moddels
class Contact(models.Model):
    
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    
    
    def __self__(self):
        return self.name
    
    