from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('success.html', home_page),
    path('cancel.html', home_page),
    path('create_checkout_session', create_checkout_session),
]
