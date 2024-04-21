from django.contrib import admin
from .models import ResumeData
# Register your models here.
@admin.register(ResumeData)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','city','email','pin_code','mobile_num','profile_img','my_file']