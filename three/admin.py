from django.contrib import admin
from three.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_full_url', 'parent')
    list_filter = ('parent', 'name')
    readonly_fields = ('url',)

    def get_full_url(self, obj):
        return obj.get_full_url()

    get_full_url.short_description = 'Полный URL-адрес'
