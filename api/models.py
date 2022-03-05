from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     for user in User.objects.all():
#       Token.objects.get_or_create(user=user)
#     if created:
#         Token.objects.create(user=instance)




class Notes(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    note = models.TextField()
   



class TrashNotes(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    note = models.TextField()
   

