from django.contrib import admin

# Register your models here.
from app.models import *
class customizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['url','email']
    list_editable=['name']
    search_fields=['name']
    list_filter=('name',)
    list_per_page=1
class customizeAccessRecord(admin.ModelAdmin):
    list_display=['name','date','author']
    list_display_links=['name','date']
    list_editable=['author']
    search_fields=['name']
    list_filter=('name',)
    list_per_page=1
admin.site.register(Topic)
admin.site.register(Webpage,customizeWebpage)
admin.site.register(AccessRecord,customizeAccessRecord)