from app.tasks.models.character import Character
from app.serializers import CharacterSerializer
from rest_framework import generics, permissions

class CharacterDetailView(generics.RetrieveAPIView):
    """Get the current user's character stats"""
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user.character

class LevelUpView(generics.UpdateAPIView):
    """Example of game action endpoint"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        character: Character = self.request.user.character
        if character.gain_experience():
            serializer.save()
