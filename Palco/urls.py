from rest_framework import routers
from Palco.views import MusicoView, InstrumentoView

router = routers.DefaultRouter()
router.register (r'Musicos', MusicoView)
router.register (r'Instrumentos', InstrumentoView)


urlpatterns = router.urls