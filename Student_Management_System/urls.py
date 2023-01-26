from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student/', include('Student.urls')),
    path('College/', include('College.urls')),
]
