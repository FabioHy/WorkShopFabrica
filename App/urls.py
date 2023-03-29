from rest_framework import routers
from App.views import LuisAmigoViewSet

router = routers.DefaultRouter()
router.register(r'', LuisAmigoViewSet)

urlpatterns = router.urls
