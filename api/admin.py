from django.contrib import admin

# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin
from .models import Notes,TrashNotes
# Register your models here.
admin.site.register(Notes)
admin.site.register(TrashNotes)
TokenAdmin.raw_id_fields = ['user']