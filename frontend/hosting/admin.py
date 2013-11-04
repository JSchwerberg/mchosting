from django.contrib import admin
from hosting.models import MinecraftPlan, MinecraftFeature, MinecraftService
from django.core import serializers

class MinecraftPlanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name', 'short_desc', 'desc', 'price', 'active']}),
        ('Service Specific',    {'fields': ['max_memory', 'max_storage', 'included_features']}),
    ]
    list_display = ('name', 'short_desc', 'price')
    actions = ['deactivate', 'activate']
    
    def deactivate(self, request, queryset):
        queryset.update(active=False)
    deactivate.short_description = "Remove selected plans from site"

    def activate(self, request, queryset):
        queryset.update(active=True)
    activate.short_description = "Add selected plans to site"



class MinecraftFeatureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name', 'internal_name', 'short_desc', 'desc', 'price', 'active']}),
        ('Service Specific',    {'fields': ['required_memory', 'required_storage']})
    ]
    list_display = ('name', 'short_desc', 'price')

    def deactivate(self, request, queryset):
        queryset.update(active=False)
    deactivate.short_description = "Remove selected features from site"
    
    def activate(self,request, queryset):
        queryset.update(active=True)
    activate.short_description = "Add selected features to site"

class MinecraftServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    actions = ['resend_json']

    def resend_json(self, request, queryset):
        pass
    resend_json.short_description = "Update selected servers on back-end"



admin.site.register(MinecraftPlan, MinecraftPlanAdmin)
admin.site.register(MinecraftFeature, MinecraftFeatureAdmin)
admin.site.register(MinecraftService, MinecraftServiceAdmin)
