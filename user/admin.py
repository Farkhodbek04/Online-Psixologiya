from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(BlogReview)
admin.site.register(BlogImage)
admin.site.register(ContactUs)
