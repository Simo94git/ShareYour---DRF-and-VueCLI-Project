import locale
from rest_framework import serializers
from articles.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
	author = serializers.StringRelatedField(read_only=True)
	created_at = serializers.SerializerMethodField(read_only=True)
	likes_count = serializers.SerializerMethodField(read_only=True)
	slug = serializers.SlugField(read_only=True)
	comments_count = serializers.SerializerMethodField(read_only=True)
	user_has_liked = serializers.SerializerMethodField(read_only=True)
	user_has_commented = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Article
		exclude = ["likes", "updated_at", "image"]

	def get_created_at(self, instance):
		return instance.created_at.strftime('%d %B %Y') 
										#formattazione date personalizzata

	def get_comments_count(self, instance):
		return instance.comments.count()


	def get_likes_count(self, instance):
		return instance.likes.count()

	def get_user_has_liked(self, instance):
		request = self.context.get("request")
		return instance.likes.filter(pk=request.user.pk).exists()
		#ritornerà True o False se lo user ha votato o meno una risposta

	def get_user_has_commented(self, instance):
		request = self.context.get("request")
		return instance.comments.filter(author=request.user).exists()
		



class CommentSerializer(serializers.ModelSerializer):

	author = serializers.StringRelatedField(read_only=True)
	created_at = serializers.SerializerMethodField(read_only=True)
	likes_count = serializers.SerializerMethodField(read_only=True)
	user_has_voted = serializers.SerializerMethodField(read_only=True)

	#per onSubmit() in CommentEditor.vue
	article_slug = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Comment
		exclude = ["article", "voters", "updated_at"]

	def get_created_at(self, instance):
		return instance.created_at.strftime('%d %B %Y') 
										#formattazione date personalizzata

	def get_likes_count(self, instance):
		return instance.voters.count()

	def get_user_has_voted(self, instance):
		request = self.context.get("request")
		return instance.voters.filter(pk=request.user.pk).exists()
		#ritornerà True o False se lo user ha votato o meno una risposta

	def get_article_slug(self, instance):
		return instance.article.slug


