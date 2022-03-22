from rest_framework import viewsets
from pocket.manager.serializers import ActivitySerializer
from pocket.manager.models import Activity


class ActivityViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    serializer_class = ActivitySerializer
    user = request.user

    def get_queryset(self):
        
        queryset = Activity.objects.filter(owner=self.request.user.id)


