
# Create your models here.
from django.db import models

# Create your models here.

class StudentModel(models.Model):
    
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField(default='Address')
    # mail_address = models.EmailField()
    mobile = models.TextField(default='+880')
      
    def __str__(self):
        return self.name
    
    
class AssetModel(models.Model):
    
    assetid = models.IntegerField(primary_key=True)
    assettype = models.CharField(max_length=30)
    condition = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.asset_id
    
       
       
class EmployeeModel(models.Model):
    
    employeeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    employeeemail = models.EmailField()
    mobile = models.CharField(max_length=30)
    def __str__(self):
        return self.employee_id
    
    
    
    
class AssetCheckOutModel(models.Model):
    
    asset = models.ForeignKey(AssetModel, on_delete=models.CASCADE)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=True)
    condition = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.asset} {'Check-out' if self.check_out else 'Return'} by {self.employee} on {self.timestamp}"
    

    
 