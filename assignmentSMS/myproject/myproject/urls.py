from django.urls import path, include
from rest_framework import routers
from myapp.views import CompanyViewSet, ClientViewSet, ClientUserViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'client-users', ClientUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

