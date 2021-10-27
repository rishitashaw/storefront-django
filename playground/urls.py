from django.urls.conf import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello)
]
