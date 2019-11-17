from django.contrib import admin
from django.urls import path

from remempill import views
from remempill.views import *


urlpatterns = [
    # path('', views.index, name='index'),
    path('pillcase', views.pillcase, name="pillcase"),
    path('', Index.as_view()),
]

admin.site.site_header = 'RememPill Administration Site'
admin.site.site_title = 'RememPill Administration Site'
