from django.urls import include, path
from rest_framework import routers

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitlesViewSet, UserViewSet,
                    get_token_for_user, send_confirmation_code)

router_api_v1 = routers.DefaultRouter()
router_api_v1.register('users', UserViewSet, basename='users')
router_api_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                       ReviewViewSet, basename='reviews')
router_api_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                       r'/comments', CommentViewSet, basename='comments')
router_api_v1.register('categories', CategoriesViewSet, basename='categories')
router_api_v1.register('titles', TitlesViewSet, basename='titles')
router_api_v1.register('genres', GenresViewSet, basename='genres')
registration = [
    path('signup/', send_confirmation_code, name='signup'),
    path('token/', get_token_for_user, name='token'),
]

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('v1/auth/', include(registration))
]
