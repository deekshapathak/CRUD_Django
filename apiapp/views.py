from django.shortcuts import render
from django.http import JsonResponse
from . serializers import TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'LIST':'/task-list',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create',
        'Update': '/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }
  
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

    #for delete
@api_view(['DELETE'])
# def taskDelete(request,pk):
#     try:
#      task = Task.objects.get(id=pk)
#      task.delete()

#     return JsonResponse({'message': 'Task deleted successfully'}, status=200)
#    except Task.DoesNotExist:
#      return JsonResponse({'error': 'Task not found'}, status=404)

    
    
@api_view(['DELETE'])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)



