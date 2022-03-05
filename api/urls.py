from django.urls import path
from . import views


urlpatterns = [
    path('api/',views.listAPIView.as_view(),name='getApi'),
    path('addnote',views.addNoteView.as_view(),name='createNote'),
    path('trashnotes',views.trashNotes.as_view(),name='trashNotes'),
    path('updatenote',views.updateNote.as_view(),name='updatenote')
    # path('api-auth/', views.ExampleView.as_view(),name='exp'),


]