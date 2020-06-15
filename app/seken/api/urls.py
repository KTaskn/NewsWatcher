from rest_framework import routers
from .views import NewspaperViewSet, WordViewSet

router = routers.DefaultRouter()
router.register('newspapers', NewspaperViewSet)
router.register('words', WordViewSet)