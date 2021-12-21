from django.contrib import admin
from.models import Post, BLogComment

# Register your models here.
admin.site.register((Post, BLogComment))


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('tinyinject.js')
