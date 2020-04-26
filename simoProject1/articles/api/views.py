from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article, Comment
from articles.api.serializers import ArticleSerializer, CommentSerializer
from articles.api.permissions import IsAuthorOrReadOnly

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all().order_by("-created_at")
	lookup_field = "slug" #se non lo si definisce, il default è "pk"
	serializer_class = ArticleSerializer
	permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


# crea commento per una specifico articolo(un utente può mandare
# un solo commento per ogni domanda)
class CommentCreateAPIView(generics.CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		request_user = self.request.user
		kwargs_slug = self.kwargs.get("slug")
		article = get_object_or_404(Article, slug=kwargs_slug)

		if article.comments.filter(author=request_user).exists():
			raise ValidationError("Non puoi commentare piu volte lo stesso articolo")

		serializer.save(author=request_user, article=article)


# lista di commenti a specifica istanza di Article
class ArticleCommentListAPIView(generics.ListAPIView):
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticated]

	#commenti associati a una specifica istanza di Article
	def get_queryset(self):
		kwargs_slug = self.kwargs.get("slug")
		return Comment.objects.filter(article__slug=kwargs_slug).order_by("-created_at")


class SingleComment_RUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class CommentLikeAPIView(APIView):
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticated]

	def delete(self, request, pk):
		comment = get_object_or_404(Comment, pk=pk)
		user = self.request.user
		comment.voters.remove(user)
		comment.save()

		serializer = self.serializer_class(comment,
										context={"request": request})

		return Response(serializer.data, status=status.HTTP_200_OK)


	def post(self, request, pk):
		comment = get_object_or_404(Comment, pk=pk)
		user = self.request.user
		comment.voters.add(user)
		comment.save()

		serializer = self.serializer_class(comment,
										context={"request": request})

		return Response(serializer.data, status=status.HTTP_200_OK)

class ArticleLikeAPIView(APIView):
	serializer_class = ArticleSerializer
	permission_classes = [IsAuthenticated]

	def delete(self, request, **kwargs):
		kwargs_slug = self.kwargs.get("slug")
		article = get_object_or_404(Article, slug=kwargs_slug)
		user = self.request.user
		article.likes.remove(user)
		article.save()

		serializer = self.serializer_class(article,
										context={"request": request})

		return Response(serializer.data, status=status.HTTP_200_OK)


	def post(self, request, **kwargs):
		kwargs_slug = self.kwargs.get("slug")
		article = get_object_or_404(Article, slug=kwargs_slug)
		user = self.request.user
		article.likes.add(user)
		article.save()

		serializer = self.serializer_class(article,
										context={"request": request})

		return Response(serializer.data, status=status.HTTP_200_OK)


