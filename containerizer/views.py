from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import App, Container, RunningHistoryRecord
from .serializers import AppSerializer, RunningHistoryRecordSerializer, ContainerSerializer
from .utils import run, stop, record_history
from datetime import datetime


class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer
    
    def get_queryset(self):
        return App.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RunningHistoryView(ListAPIView):
    serializer_class = RunningHistoryRecordSerializer

    def get_queryset(self):
        return RunningHistoryRecord.objects.filter(container_id__app__user=self.request.user.id)


class RunNewContainerView(APIView):

    def post(self, request, app_id):
        app = App.objects.get(id=app_id)

        container_id = run(app)
        current_status = 'Running'

        container = Container.objects.create(
                                        app=app, 
                                        container_id=container_id, 
                                    )
        
        record_history(container, current_status)
        serializer = ContainerSerializer(container)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RunContainerView(APIView):
    
    def get(self, request, container_id):

        container = Container.objects.get(container_id=container_id)
        app = container.app

        container_id = run(app)

        current_status = 'Running'
        record_history(container, current_status)

        serializer = ContainerSerializer(container)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StopContainerView(APIView):

    def get(self, request, container_id):

        current_status = 'Finished'

        container = get_object_or_404(Container, container_id=container_id)
        stop(container.container_id)

        container.status = current_status
        record_history(container, current_status)

        container.stopped_at = datetime.now()
        container.save()

        return Response(status=status.HTTP_204_NO_CONTENT)