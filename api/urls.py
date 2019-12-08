from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('recipe', RecipeView)

urlpatterns = [
    url('', include(router.urls)),
]
