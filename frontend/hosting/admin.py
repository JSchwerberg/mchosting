from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from hosting.models import MinecraftPlan, MinecraftFeature, MinecraftService
import simplejson

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
        for obj in queryset:
            fields = {}
            fields = {
                'action': 'update'
                'id': obj.id
                'memory': obj.minecraftplan.max_memory
                'storage': obj.minecraftplan.max_storage
            }
            for f in obj.minecraftfeature:
            features = []
            features += feature.internal_name
            fields['features'] = ",".join(features)
            json = simplejson.dumps(fields)
            # send_json(fields)
    resend_json.short_description = "Update selected servers on back-end"



admin.site.register(MinecraftPlan, MinecraftPlanAdmin)
admin.site.register(MinecraftFeature, MinecraftFeatureAdmin)
admin.site.register(MinecraftService, MinecraftServiceAdmin)
