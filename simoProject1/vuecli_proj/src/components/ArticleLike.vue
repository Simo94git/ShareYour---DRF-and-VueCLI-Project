<template lang="html">
	<div class="like-article">
			<button
			class="btn"
			@click="toggleArticleLike"
			:class="{
				'btn-danger': userLikedArticle,
				'btn-outline-danger': !userLikedArticle,
			}"
			>
				<strong>{{ likes_numbers }} Mi piace </strong>
			</button>
	</div>
</template>





<script>
import { apiService } from "../common/api.service.js";

export default{
	name: "ArticleLike",
	props:{
		article:{
			type: Object,
			required: true
	}
},
	data(){
		return{
			userLikedArticle: this.article.user_has_liked,
			likes_numbers: this.article.likes_count
		}
	},
	methods:{

	toggleArticleLike(){
			this.userLikedArticle === false 
			? this.likeArticle() 
			: this.unLikeArticle()
		},
	likeArticle(){
			this.userLikedArticle = true;
			this.likes_numbers += 1;
			let endpoint =  `/api/articles/${this.article.slug}/like/`;
			apiService(endpoint, "POST");
	},
	unLikeArticle(){
			this.userLikedArticle = false;
			this.likes_numbers -= 1;
			let endpoint =  `/api/articles/${this.article.slug}/like/`;
			apiService(endpoint, "DELETE");
		}   //risolvi bug dei Mi piace
	}
}


</script>





<style lang="css">
	
</style>