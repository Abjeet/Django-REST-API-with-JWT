from django.conf.urls import url
from apis import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [



url('api_overview',views.api_overview,name='api_overview'),
url('task-list',views.task_list,name='task-list'),
url('create-task',views.create_task,name='create-task'),
url('task-details/(?P<pk>[0-9]+)$',views.task_details,name='task_details'),
url('update-task/(?P<pk>[0-9]+)$',views.update_task,name='update_task'),
url('delete-task/(?P<pk>[0-9]+)$',views.delete_task,name='delete_task'),
url('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),




]