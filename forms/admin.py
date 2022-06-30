from django.contrib import admin
from .models import Student, Post, Mail, Choice
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'roll_number')


admin.site.register(Student, StudentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender')


admin.site.register(Post, PostAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice


class MailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject Information', {'fields': ['subject']}),
        ('Message', {'fields': ['message']}),
        ('Sender Information', {'fields': ['sender']}),
        ('CC Information', {'fields': ['cc_myself']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('sender', 'subject')


admin.site.register(Mail, MailAdmin)


