from rest_framework import routers
from .views import NewspaperViewSet, WordViewSet, WordRankingViewSet

router = routers.DefaultRouter()
router.register('newspapers', NewspaperViewSet)
router.register('words', WordViewSet)
router.register('wordranking', WordRankingViewSet)