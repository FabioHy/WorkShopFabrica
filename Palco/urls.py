from rest_framework import routers
from django.urls import path, include
from .views import MusicoView, InstrumentoView, MusicoEditar, InstrumentoEditar

#from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'musicos', MusicoView)
router.register (r'instrumentos', InstrumentoView)


urlpatterns = [
    path('musicos/', MusicoView.as_view()),
    path('musicos/<int:pk>/', MusicoEditar.as_view()),
    path('instrumentos/', InstrumentoView.as_view()),
    path('instrumentos/<int:pk>/', InstrumentoEditar.as_view()),
]