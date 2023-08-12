from django.db import models

# Create your models here.

# default db_table => <app_name>_<model_name>
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    email = models.EmailField(null=True)
    
    class Meta:
        db_table = "persons_app_person"
    