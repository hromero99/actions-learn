
from django.contrib import admin
from django.urls import path
from person.views import PersonViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    path("person/", PersonViewSet.as_view())
]
