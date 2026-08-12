
from django.urls import include, path
from rest_framework import routers

from api.views import CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeViewSet) 


urlpatterns = [
  path('',include(router.urls))
]
