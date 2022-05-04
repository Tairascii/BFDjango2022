from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.models import Blog, Skin
from api.serializers import BlogSerializer, SkinSerializer

import logging
logger = logging.getLogger('django')


class BlogListAPIView(APIView):
    def get_objects(self):
        return Blog.objects.all()

    def get(self, request):
        blogs = self.get_objects()
        serializer = BlogSerializer(blogs, many=True)
        logger.info('Blogs sent')
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAuthenticated,)


class BlogDetailAPIView(APIView):
    def get_object(self, pk):
        return Blog.objects.get(id=pk)

    def get(self, blog_id=None):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        logger.info('Blog sent')
        return Response(serializer.data)

    def put(self, request, blog_id=None):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request, blog_id=None):
        blog = self.get_object(blog_id)
        blog.delete()
        logger.info('Blog deleted')
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAuthenticated,)


class SkinListAPIView(APIView):
    def get_objects(self, rarity):
        if rarity == 'XE':
            return Skin.exclusive.all()
        if rarity == 'SE':
            return Skin.select.all()
        if rarity == 'DE':
            return Skin.deluxe.all()
        if rarity == 'PE':
            return Skin.premium.all()
        return Skin.skins.all()

    def get(self, request):
        skins = self.get_objects(self.request.GET.get('q', None))
        serializer = SkinSerializer(skins, many=True)
        logger.info('Skins sent')
        return Response(serializer.data)

    def post(self, request):
        serializer = SkinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkinDetailAPIView(APIView):
    def get_object(self, pk):
        return Skin.skins.get(id=pk)

    def get(self, skin_id=None):
        skin = self.get_object(skin_id)
        serializer = SkinSerializer(skin)
        logger.info('Skin sent')
        return Response(serializer.data)

    def put(self, request, skin_id=None):
        skin = self.get_object(skin_id)
        serializer = SkinSerializer(instance=skin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request, skin_id=None):
        skin = self.get_object(skin_id)
        skin.delete()
        logger.info('Skin deleted')
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser,)



