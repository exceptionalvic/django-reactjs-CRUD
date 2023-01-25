from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet, basename='users')

# urlpatterns = [
#     path('users/', UserView.as_view(), name='user_view'),
#     path('articles/', ArticleList.as_view(), name='article_list'),
#     path('article/<int:id>/', ArticleDetail.as_view(), name='article_detail'),
# ]

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

# urlpatterns = router.urls