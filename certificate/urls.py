from django.conf.urls import url
from api import views
from django.urls import path

urlpatterns = [
    url(r'^participant/', views.participant_list),
    url(r'^certificate/(?P<email>[\s\S]*)$', views.certificate)
]

