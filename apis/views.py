from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tasks
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt import authentication


@api_view(['GET'])
def api_overview(request):
         # permission_classes = (permissions.IsAuthenticated,)
         # authentication_classes = (authentication.JWTAuthentication,)
         api_urls={
             'List':'task-list',
             'Details':'task-details/<str:pk>',
             'Create':'create-task',
             'Update':'update-task/<str:pk>',
             'Delete':'delete-task/<str:pk>',

         }
         return Response(api_urls)


@api_view(['GET'])
def task_list(request):

    all_task=Tasks.objects.all()
    serializer=TaskSerializer(all_task,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(data="all fields req", status=status.HTTP_400_BAD_REQUEST )


@api_view(['GET'])
def task_details(request, pk):
    if Tasks.objects.filter(pk=pk).count():
        get_task=Tasks.objects.get(pk=pk)
        return Response(TaskSerializer(get_task,many=False).data)
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_task(request, pk):

    if not Tasks.objects.filter(pk=pk).count():
        return Response( status=status.HTTP_400_BAD_REQUEST)
    snippet = Tasks.objects.get(pk=pk)
    serializer=TaskSerializer(snippet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def delete_task(request, pk):
    if not Tasks.objects.filter(pk=pk).count():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    snippet = Tasks.objects.get(pk=pk)
    snippet.delete()
    return Response( status=status.HTTP_201_CREATED)

