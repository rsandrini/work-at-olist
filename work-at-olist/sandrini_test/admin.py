# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Channel, Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class ChannelAdmin(admin.ModelAdmin):
    inlines = (CategoryInline, )
    search_fields = ['name']


admin.site.register(Channel, ChannelAdmin)