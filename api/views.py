from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView, RetrieveAPIView,UpdateAPIView
from rest_framework.views import APIView
from .models import Notes,TrashNotes
from .serializers import NoteSerializer, TrashNoteSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.


class listAPIView(ListAPIView):
        # permission_classes = (IsAuthenticated)
        permission_classes = [IsAuthenticated]
        queryset = Notes.objects.all()
        serializer_class = NoteSerializer
        
class addNoteView(CreateAPIView):
         permission_classes = [IsAuthenticated]
         queryset = Notes.objects.all()
         serializer_class = NoteSerializer

class  trashNotes(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TrashNotes.objects.all()
    serializer_class = TrashNoteSerializer


class updateNote(APIView):
        permission_classes = [IsAuthenticated]
        def update(self,request):
                 if request.data != None:
                  nid = request.data.get('id')
                  updatedNote = request.data.get('body')
                  record = Notes.objects.get(id=nid)
                  record.note = updatedNote
                  record.save()
                  return JsonResponse('Item Updated Sucessfully...')
