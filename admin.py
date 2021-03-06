from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine_libations.models import PostWithLibation

#readonly_fields = ("libation_app_name",)
blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
#blog_fieldsets.insert(0, 
#[0][1]["fields"].insert(0, "libation_app_name")

class PostLibationAdmin(BlogPostAdmin):
    fieldsets = [
        ('Libation', {
                'fields': [ 'post_libation_title', 'post_libation_type_choice', 'post_libation_recipe','post_libation_image']}),
        ]
    fieldsets.insert(0, BlogPostAdmin.fieldsets[0])

#admin.site.register(BlogPost)
#admin.site.unregister(BlogPost)
admin.site.register(PostWithLibation, PostLibationAdmin)
