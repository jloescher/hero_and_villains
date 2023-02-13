from django.shortcuts import render, get_object_or_404
from rest_framework import generics
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
        type = request.query_params.get("type")
        if type:
            if type == "hero":
                queryset = Super.objects.filter(super_type__type="Hero")
            elif type == "villain":
                queryset = Super.objects.filter(super_type__type="Villain")
            else:
                queryset = Super.objects.none()
            serializer = SuperSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            heroes = Super.objects.filter(super_type__type="Hero")
            villains = Super.objects.filter(super_type__type="Villain")
            custom_response = {"heroes": heroes, "villains": villains}
            return Response(custom_response)


class SuperDetailView(generics.RetrieveAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer


class SuperUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer

    def perform_update(self, serializer):
        super_id = self.kwargs["pk"]
        super = Super.objects.get(id=super_id)
        serializer.save()


class SuperDeleteView(generics.DestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer
