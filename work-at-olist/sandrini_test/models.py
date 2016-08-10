from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Channel(models.Model):
    name = models.CharField("Channel name", max_length=255, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=255, blank=True)

    class Meta:
        app_label = 'sandrini_test'
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug is None:
            self.slug = slugify(self.name)
        super(Channel, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField("Category name", max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    channel = models.ForeignKey(Channel, verbose_name="Channel", related_name="categories")
    top_category = models.ForeignKey("Category", verbose_name="Top Category", blank=True, null=True)

    class Meta:
        app_label = 'sandrini_test'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = (('channel', 'name', 'top_category'),)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug is None:
            if self.top_category:
                self.slug = slugify("%s %s %s" % (self.channel.name, self.top_category.name, self.name))
            else:
                self.slug = slugify("%s %s" % (self.channel.name, self.name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
