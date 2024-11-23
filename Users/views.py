from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from Users.serializers import UserSerializer
from Users.permissions import UserPermission

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return []
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)