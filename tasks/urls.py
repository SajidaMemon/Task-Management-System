from django.urls import path, include 
from . import views


# this is for rest api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'labels', views.LabelView)
router.register(r'tasks' , views.TaskView)


urlpatterns = [
    path('', views.index, name="name"),
    path('api/', include(router.urls)),
]

# http://localhost:8000/api/labels/
# http://localhost:8000/api/tasks/
