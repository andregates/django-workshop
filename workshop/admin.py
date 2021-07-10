from django.contrib import admin
from workshop.models import Image, Interest, Student

# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['image', 'image_tag']
    list_display = ['image', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Interest)
admin.site.register(Student)

