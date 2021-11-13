from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)