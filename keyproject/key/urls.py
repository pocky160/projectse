from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib import admin

urlpatterns = [
    path('',Homepage, name='home-page'),
    path('booking/',Booking, name='booking-page'),
    path('history/',History, name = 'history-page'),
    path('notification/',Notification, name = 'notification-page'),
    # path('asadmin/', admin.site.urls, name = 'asadmin-page')
]