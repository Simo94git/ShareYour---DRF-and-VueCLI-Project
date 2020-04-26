from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.api.views import (ArticleViewSet,
								CommentCreateAPIView,
								ArticleCommentListAPIView,
								SingleComment_RUDAPIView,
								CommentLikeAPIView,
								ArticleLikeAPIView)


router = DefaultRouter()
router.register(r"articles", ArticleViewSet)

urlpatterns = [
	path("", include(router.urls)),
	
	path("articles/<slug:slug>/comment/",
		CommentCreateAPIView.as_view(),
		name="create-comment" ),

	path("articles/<slug:slug>/comments/",
		ArticleCommentListAPIView.as_view(),
		name="comments-list"),

	path("comments/<int:pk>/",
		SingleComment_RUDAPIView.as_view(),
		name="comment-detail"),

	path("comments/<int:pk>/like/",
		CommentLikeAPIView.as_view(),
		name="comments-like"),

	path("articles/<slug:slug>/like/",
		ArticleLikeAPIView.as_view(),
		name="articles-like"),
]