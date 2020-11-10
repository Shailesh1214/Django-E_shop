from django.urls import path
from .views import index, signup, Login 
urlpatterns=[
    path('', index, name='homepage'),
    path('signup', signup),
    path('Login',Login)

]