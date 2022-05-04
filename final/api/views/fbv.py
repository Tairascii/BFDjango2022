from api.models import Gun, Enchantment
from api.serializers import GunSerializer, EnchantmentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging
logger = logging.getLogger('django')


@api_view(['GET'])
def get_guns(request):
    guns = Gun.objects.all()
    serializer = GunSerializer(guns, many=True)
    logger.info('Guns sent')
    return Response(serializer.data)


@api_view(['GET'])
def get_enchantment(request):
    enchantments = Enchantment.objects.all()
    serializer = EnchantmentSerializer(enchantments, many=True)
    logger.info('Enchantments sent')
    return Response(serializer.data)