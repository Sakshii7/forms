from django.contrib import admin
from .models import Student, Post
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'roll_number')


admin.site.register(Student, StudentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender')


admin.site.register(Post, PostAdmin)
