from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    image = models.TextField()

    class Meta:
        abstract = True


class Gun(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)



class Enchantment(models.Model):
    name = models.CharField(max_length=300)
    level = models.IntegerField()
    type = models.CharField(max_length=300)


class SelectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rarity='SE')


class DeluxeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rarity='DE')


class PremiumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rarity='PE')


class ExclusiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rarity='XE')


class Skin(Item):
    rarity = models.CharField(max_length=2, choices=[('SE', 'Select Edition'),
                                                     ('DE', 'Deluxe Edition'),
                                                     ('PE', 'Premium Edition'),
                                                     ('XE', 'Exclusive Edition')])
    enchantment = models.ForeignKey(Enchantment, on_delete=models.CASCADE)
    gun = models.ForeignKey(Gun, related_name='guns', on_delete=models.CASCADE)
    skins = models.Manager()
    select = SelectManager()
    deluxe = DeluxeManager()
    premium = PremiumManager()
    exclusive = ExclusiveManager()


class Graffiti(Item):
    enchantment = models.ForeignKey(Enchantment, on_delete=models.CASCADE, null=True)
    isAnimated = models.BooleanField()


class Charm(Item):
    enchantment = models.ForeignKey(Enchantment, on_delete=models.CASCADE, null=True)
    event = models.CharField(max_length=300)


class User(models.Model):
    nick = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    isModer = models.BooleanField()

    class Meta:
        abstract = True


class Visitor(AbstractUser):
    username = models.CharField(max_length=300, unique=True, null=True)
    password = models.CharField(max_length=300)
    isModer = models.BooleanField(null=True)
    isBanned = models.BooleanField(null=True)
    image = models.ImageField(null=True, upload_to='imgs/')
    # wishlist = models.ManyToManyField(Skin, related_name='skin')


class Blog(models.Model):
    title = models.TextField()
    desc = models.TextField()
    file = models.FileField(null=True, upload_to='documents/')
    user = models.ForeignKey(Visitor, on_delete=models.CASCADE)











