from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer


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


class SuperDetailView(generics.RetrieveAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer


class SuperUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        serializer = self.perform_update(self.get_serializer())
        return Response(serializer.data)


class SuperDeleteView(generics.DestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer
    http_method_names = ["DELETE"]
    permission_classes = [
        permissions.AllowAny,
    ]
    allowed_methods = [
        "DELETE",
    ]

    def delete(self, request, *args, **kwargs):
        if request.method != "DELETE":
            print(request.method)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        super = self.get_object()
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
