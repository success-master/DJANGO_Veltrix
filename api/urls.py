from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('requests', views.RequestView)

urlpatterns = [
    path('', include(router.urls))
    # path('', RequestAll.as_view()),
    # path('<int:pk>/', RequestDetail.as_view())

]
