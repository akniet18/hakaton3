from .views import *
from django.urls import path, include


urlpatterns = [
	path('', ArticleView.as_view()),
	path('<int:pk>/', UserView.as_view()),
	path('login/', Login.as_view()),
	path('register/', Register.as_view()),

	path('institut/', InsView.as_view()),
	path('search_user/', SearchUserView.as_view())
]