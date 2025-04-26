from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Process
from .serializers import ProcessSerializer
from .auth import SimpleAPIKeyAuthentication
from django.utils import timezone

class ProcessDataReceiver(APIView):
    authentication_classes = [SimpleAPIKeyAuthentication]

    def post(self, request):
        hostname = request.data.get('hostname')
        processes = request.data.get('processes', [])

        for proc in processes:
            proc['hostname'] = hostname
            proc['timestamp'] = timezone.now()
            serializer = ProcessSerializer(data=proc)
            if serializer.is_valid():
                serializer.save()

        return Response({"status": "success"}, status=status.HTTP_201_CREATED)

class ProcessDataViewer(APIView):
    def get(self, request):
        hostname = request.GET.get('hostname')
        latest = Process.objects.filter(hostname=hostname).order_by('-timestamp')[:100]
        serializer = ProcessSerializer(latest, many=True)
        return Response(serializer.data)
    
def frontend_view(request):
    return render(request, 'index.html')