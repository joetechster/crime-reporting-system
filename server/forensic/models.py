# models.py (in your app)
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    passport = models.ImageField(upload_to='passports/', blank=True, verbose_name="Passport (Photo)")
    address = models.TextField(blank=True, verbose_name="Address")

    def __str__(self):
        return self.email
      
    class Meta:
      verbose_name = "User"
      verbose_name_plural = "Users"
    
class CrimeCode(models.Model): 
    code = models.TextField(blank=False, verbose_name="Code", primary_key=True)  
    description = models.TextField(blank=False, verbose_name="Code Description") 
    
class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Reporter", blank=False) 
    crime_code = models.ForeignKey(CrimeCode, on_delete=models.DO_NOTHING, verbose_name="Crime Code", blank=False) 
    crime_statement = models.TextField(blank=False, verbose_name="Statement") 
    crime_status = models.TextField(choices=(('pending', 'pending'), ('approved', 'approved')), default='approved')
    created_at = models.DateTimeField(auto_now_add=True)
