from django.contrib import admin
from blog.models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title',)}
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
# Register your models here.
