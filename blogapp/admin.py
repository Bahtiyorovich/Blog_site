from django.contrib import admin

from blogapp.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'publish', 'status',)
    list_filter = ('status','publish','created', 'author',)
    search_fields = ('title','body',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)