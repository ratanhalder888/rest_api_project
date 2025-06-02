from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact
from myapp.serializers import Contact_Serializer

# Create your views here.
@csrf_exempt
def api_list(request):
    if request.method == 'GET':
        api_var = Contact.objects.all()
        serializer = Contact_Serializer(api_var, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Contact_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def api_detail(request, pk):
    try:
        api_var = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Contact_Serializer(api_var)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Contact_Serializer(api_var, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        api_var.delete()
        return HttpResponse(status=204)