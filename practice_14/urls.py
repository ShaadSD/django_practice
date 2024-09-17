
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('inpuapp.urls')),
    path('models/',include('models_inp.urls')),
]