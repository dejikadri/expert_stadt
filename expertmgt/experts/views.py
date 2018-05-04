from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expert
from .serializers import ExpertSerializer
from django.http import Http404



class ExpertList(APIView):
    def get(self, request):

        experts_list = Expert.objects.all()
        serialized_experts = ExpertSerializer(experts_list, many=True)
        return Response(serialized_experts.data)

    def post(self, request):
        serializer = ExpertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpertDetail(APIView):
    def get_object(self, pk):
        try:
            return Expert.objects.get(pk=pk)
        except Expert.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        expert = self.get_object(pk)
        serializer = ExpertSerializer(expert)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        expert = self.get_object(pk)
        serializer = ExpertSerializer(expert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """ updates the expert to marked  for deletion field to """

        expert = self.get_object(pk)
        serializer = ExpertSerializer(expert, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)