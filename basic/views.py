from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def sample(request):
    return HttpResponse("hello world")

def sample1(request):
    return HttpResponse("Welcome to Django")

def sampleinfo(request):
    # data={"name":'Krishna','age':25,'city':'hyderabad'}
    data={"result":[4,6,8,9]}
    return JsonResponse(data,safe=False)

def dynamicResponse(request):
    name=request.GET.get("name",'Krishna')
    city=request.GET.get("city",'hyd')
    return HttpResponse(f"Hello {name} from {city}")

def add(request):
    # get two numbers from the query parameters (URL)
    num1 = request.GET.get('a', 0)
    num2 = request.GET.get('b', 0)

    try:
        # convert them to integers and calculate sum
        total = int(num1) + int(num2)
        return HttpResponse(f"The sum of {num1} and {num2} is {total}")
    except ValueError:
        return HttpResponse("Please enter valid numbers!")
    

    
