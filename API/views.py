from rest_framework.decorators import api_view 
from API.serializer import TaskSerializer
from rest_framework.response import Response
from API.models import Task

# Create your views here.

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serilized_data= TaskSerializer(data=request.data)
        if serilized_data.is_valid():
            serilized_data.save()
            resp= {'msg':'Task Created Successfully.!'}
            return Response(resp)
        # if data is invalid
        return Response(serilized_data._errors)

@api_view(['GET'])
def retrieve(request):
    if request.method == 'GET':
        allTasks= Task.objects.all()
        serialized_data= TaskSerializer(allTasks,many=True)
        return Response(serialized_data.data)

@api_view(['GET'])
def retrieveByid(request,ID):
    if request.method == 'GET':
        try:
            task= Task.objects.get(pk=ID)
            serialized= TaskSerializer(task)
            return Response(serialized.data)
        except Exception as e: 
            resp= {'msg':'not found'}
            return Response(resp)

@api_view(['PUT'])
def update(request,ID):
    if request.method== 'PUT':
        task= Task.objects.get(pk=ID)
        serialized= TaskSerializer(task,data=request.data,partial=True)
        if serialized.is_valid():
            serialized.save()
            resp= {'msg':'Task Updated Successfully.!'}
            return Response(resp)
        # if data is invalid
        return Response(serialized._errors)

@api_view(['DELETE'])
def delete(request,ID):
    if request.method == 'DELETE':
        task= Task.objects.get(pk=ID)
        task.delete()
        resp= {'msg':'Task deleted Successfully.!'}
        return Response(resp)

