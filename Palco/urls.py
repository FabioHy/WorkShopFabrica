from rest_framework import routers
from django.urls import path, include
from .views import MusicoView, InstrumentoView

#from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'Musicos', MusicoView)
router.register (r'Instrumentos', InstrumentoView)


urlpatterns = router.urls