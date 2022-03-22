from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pocket import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('pocket.users.urls')),
    path('', include('pocket.manager.urls')),
    path('api/v1/', include(router))

]
