from django.contrib import admin
from . import models


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    search_fields = ('name', )
    list_editable = ('name', 'phone')
    
    
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )
    list_editable = ('name', )
    
    
class VisitAdmin(admin.ModelAdmin):
    list_display = ('date', 'latitude', 'longitude')
    search_fields = ('shop__worker__name', )


admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.Shop, ShopAdmin)
admin.site.register(models.Visit, VisitAdmin)