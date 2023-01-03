from django.urls import path
from .views import index

app_name = 'tree'

urlpatterns = [
    path('', index, name='main-page'),
]
