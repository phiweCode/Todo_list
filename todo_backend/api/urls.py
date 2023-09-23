from django.urls import path
from .views import user_creation_view

app_name = "todo_backend"

urlpatterns = [
    path('sign_up/', user_creation_view, name='sign_up')
]