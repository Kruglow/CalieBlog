from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    list_display = ('id','title','slug','created_at','get_image')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('created_at',)
    save_on_top = True
    filter_horizontal = ('category','tags',)
    readonly_fields = ('views','created_at','get_image')
    fields = ('title','slug','category','tags','content','image','get_image','views','created_at')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" height = "150">')

    get_image.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    fields = ('title', 'slug', )



class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# class AuthorAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ('id', 'name', 'slug', 'get_image')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     readonly_fields = ('get_image',)
#     fields = ('name', 'slug', 'photo', 'get_image')
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.photo.url} width="120" height = "120">')
#
#     get_image.short_description = 'Фото'



class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','email','name','text','date','parent','post',)
    list_display_links = ('id','text','name','email')
    search_fields = ('post',)
    list_filter = ('post',)
    readonly_fields = ('email','name','website','text','date','parent','post',)
    fields = ('email','name','image','text','date','parent','post',)





admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Logo)
admin.site.register(Comment, CommentAdmin)
