from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Super
from .serializers import SuperSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
class SuperView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        type = self.request.query_params.get("type", None)
        if type is not None:
            queryset = queryset.filter(super_type=type)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            heroes = Super.objects.filter(super_type="Hero")
            villains = Super.objects.filter(super_type="Villain")
            heroes_serialized = SuperSerializer(heroes, many=True)
            villains_serialized = SuperSerializer(villains, many=True)
            custom_response = {
                "heroes": heroes_serialized.data,
                "villains": villains_serialized.data,
            }
            return Response(custom_response)


@csrf_exempt
def super_detail(request, pk):
    try:
        super = Super.objects.get(pk=pk)
    except Super.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    match request.method:
        case "GET":
            super_serializer = SuperSerializer(super)
            return JSONResponse(super_serializer.data)
        case "PUT":
            super_data = JSONParser().parse(request)
            super_serializer = SuperSerializer(super, data=super_data)
            if super_serializer.is_valid():
                super_serializer.save()
                return JSONResponse(super_serializer.data)
            return JSONResponse(
                super_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        case "DELETE":
            super.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
