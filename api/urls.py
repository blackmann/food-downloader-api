from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'foods/', views.get_foods),
    url(r'download/', views.download),
]
