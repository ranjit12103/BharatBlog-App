from django.contrib import admin
from blogs.models import Category, Blog, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'short_description','category','status', 'is_featured', 'author','created_at', 'updated_at')
    search_fields = ('=id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


admin.site.register(Comment)