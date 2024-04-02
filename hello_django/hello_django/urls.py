
from django.contrib import admin
from django.urls import path
from hello_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.print_hello)
]
