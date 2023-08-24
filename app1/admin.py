

# Register your models here.
from django.contrib import admin
from . import models
# from app1.models import AssetModel, EmployeeModel,Asset_CheckOutModel


# admin.site.register(models.StudentModel)
# # admin.site.register(models.EmployeeModel)
# # admin.site.register(models.ManagerModel)

@admin.register(models.AssetModel)
class AssetModel(admin.ModelAdmin):
    list_display=['assetid', 'assettype', 'condition']
    

@admin.register(models.EmployeeModel)
class EmployeeModel(admin.ModelAdmin):
    list_display=['employeeid', 'name', 'employeeemail', 'mobile']
    
    

admin.site.register(models.AssetCheckOutModel)



# @adminchallange.register(models.Asset_CheckOutModel)
# class Asset_CheckOutModel(adminchallange.ModelAdmin):
#     list_display=['employee_id', 'name', 'employee_email', 'mobile']
    
# @admin.register(models.ManagerModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display=['name', 'city', 'designation', 'take_interview', 'hiring']
    
    
   
# @admin.register(models.Friend)
# class FriendAdmin(admin.ModelAdmin):
#     list_display=['school', 'section', 'attandance']
    
  
# @admin.register(models.Me)
# class MeAdmin(admin.ModelAdmin):
#     list_display=['school', 'section', 'attandance']
    


 
# @admin.register(models.Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'city', 'email_address']
    
 
# # @admin.register(models.Passport)
# # class PassportAdmin(admin.ModelAdmin):
# #     list_display=['id', 'user', 'pass_num', 'page','validity']
    
    

# @admin.register(models.Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display=['id', 'user', 'post_capacity', 'post_details','create_at']
    
    

# @admin.register(models.Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'school', 'address']
    
    

# @admin.register(models.Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'subject', 'mobile']