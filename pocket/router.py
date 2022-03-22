from rest_framework.routers import DefaultRouter
from pocket.manager.viewsets import ActivityViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'activity', ActivityViewSet, basename="activity")

urlpatterns = [
    path('', include(router.urls))
]
