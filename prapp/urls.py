from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'rating', Rat, basename='rating')

urlpatterns = [
	path('', include(router.urls))
	# path('', OpencvView.as_view())
	# path('<int:pk>/', RatingView.as_view()),
	# path('rating/', RatingApi.as_view())
]