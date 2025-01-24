from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')

        if not user_id:
            return Response(
                {'error': 'User ID is required in the URL to create a note.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            recipient = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {'error': 'User with the given ID was not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = serializer.save(receipient=recipient)

        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(note).data, status=status.HTTP_201_CREATED, headers=headers)
