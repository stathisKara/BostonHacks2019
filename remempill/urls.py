from django.contrib import admin
from django.urls import path
from remempill.views import *


urlpatterns = [
    path('', Index.as_view()),
]

admin.site.site_header = 'RememPill Administration Site'
admin.site.site_title = 'RememPill Administration Site'
