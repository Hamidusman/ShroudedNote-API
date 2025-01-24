from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet, basename='notes')

urlpatterns = [
    path('users/<int:user_id>/notes/', views.NoteViewSet.as_view({'post': 'create'}), name='user-notes-create'),
    path('', include(router.urls)),
]
