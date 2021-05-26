from user import views
from django.conf.urls import url


urlpatterns=[
    url('register',views.register,name='register')
]
