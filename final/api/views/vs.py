import logging
import json

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.models import Graffiti, Charm, Visitor
from api.serializers import GraffitiSerializer, CharmSerializer, VisitorSerializer
from django.contrib.auth.hashers import make_password

logger = logging.getLogger('django')


class GraffitiViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Graffiti.objects.all()

    def list(self, request):
        serializer = GraffitiSerializer(self.get_queryset(), many=True)
        logger.info('Graffities sent')
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        graffiti = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = GraffitiSerializer(graffiti)
        logger.info('Graffiti sent')
        return Response(serializer.data)


class GraffitiDetailViewSet(viewsets.ViewSet):
    def create(self, request):
        data = json.loads(request.body)
        serializer = GraffitiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Graffiti created')
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors, status=200)

    def partial_update(self, request, pk):
        graffiti = Graffiti.objects.get(id=pk)
        serializer = GraffitiSerializer(instance=graffiti, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        graffiti = Graffiti.objects.get(id=pk)
        graffiti.delete()
        logger.info('Graffiti deleted')
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser, )


class CharmViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Charm.objects.all()

    def list(self, request):
        serializer = CharmSerializer(self.get_queryset(), many=True)
        logger.info('Charms sent')
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        charm = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = CharmSerializer(charm)
        logger.info('Charm sent')
        return Response(serializer.data)


class CharmDetailViewSet(viewsets.ViewSet):
    def create(self, request):
        data = json.loads(request.body)
        serializer = CharmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Charm created')
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors, status=200)

    def partial_update(self, request, pk):
        charm = Charm.objects.get(id=pk)
        serializer = CharmSerializer(instance=charm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        charm = Charm.objects.get(id=pk)
        charm.delete()
        logger.info('Graffiti deleted')
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser,)


class VisitorViewSet(viewsets.ViewSet):
    def create(self, request):
        data = json.loads(request.body)
        data['password'] = make_password(data['password'])
        serializer = VisitorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('User created')
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors, status=200)

    def partial_update(self, request, pk):
        user = Visitor.objects.get(id=pk)
        serializer = VisitorSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors)


class ManageVisitorViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Visitor.objects.all()

    def list(self, request):
        serializer = VisitorSerializer(self.get_queryset(), many=True)
        logger.info('Visitors sent')
        return Response(serializer.data)

    def destroy(self, request, pk):
        user = Visitor.objects.get(id=pk)
        user.delete()
        logger.info('Visitor deleted')
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser,)


