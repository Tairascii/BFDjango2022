from rest_framework import serializers
from api.models import Blog, Skin, Item, Graffiti, Charm, Visitor, Enchantment, Gun


class GunSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    type = serializers.CharField()
    guns = serializers.StringRelatedField(many=True)


class EnchantmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    level = serializers.IntegerField()
    type = serializers.CharField()



class BlogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Visitor.objects.all())

    class Meta:
        model = Blog
        fields = ('id', 'title', 'desc', 'user')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'image')


class SkinSerializer(ItemSerializer):
    enchantment = serializers.PrimaryKeyRelatedField(queryset=Enchantment.objects.all())
    gun = serializers.PrimaryKeyRelatedField(queryset=Gun.objects.all())

    class Meta:
        model = Skin
        fields = ItemSerializer.Meta.fields + ('rarity', 'enchantment', 'gun')


class GraffitiSerializer(ItemSerializer):
    class Meta:
        model = Graffiti
        fields = ItemSerializer.Meta.fields + ('isAnimated',)


class CharmSerializer(ItemSerializer):
    class Meta:
        model = Charm
        fields = ItemSerializer.Meta.fields + ('event',)


class VisitorSerializer(serializers.ModelSerializer):
    # skin = serializers.StringRelatedField(many=True)

    class Meta:
        model = Visitor
        fields = ('id', 'username', 'password', 'isModer', 'isBanned')


