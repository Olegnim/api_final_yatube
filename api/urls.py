from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet,
                    UserViewSet)

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='user')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(r'posts', PostViewSet, basename='post')

router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'group', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
