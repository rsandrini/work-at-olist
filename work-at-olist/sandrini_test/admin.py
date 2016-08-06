# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Channel, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class ChannelAdmin(admin.ModelAdmin):
    inlines = (ProductInline, )
    search_fields = ['name']


admin.site.register(Channel, ChannelAdmin)