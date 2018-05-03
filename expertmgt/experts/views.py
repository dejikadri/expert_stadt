from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expert
from .serializers import ExpertSerializer


class ExpertList(APIView):
    def get(self, request):

        experts_list = Expert.objects.all()
        serialized_experts = ExpertSerializer(experts_list, many=True)
        return Response(serialized_experts.data)


