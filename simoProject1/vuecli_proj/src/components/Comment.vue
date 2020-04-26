<template>
	<div class="single-comment">
		<p class="text-muted">
			<strong>{{ comment.author }}</strong> ha commentato in data {{ comment.created_at }}
		</p>
		<p>{{ comment.comment }}</p>
		<div v-if="isCommentAuthor" class="comment-owner">
			<router-link  
			:to="{name:'comment-editor', params:{id: comment.id}  }"
			class="btn btn-secondar\y mr-1">
				<span>Modifica</span>
			</router-link>

			<button
			class="btn btn-danger"
			@click="triggerDeleteComment">
				Cancella
			</button>
		</div>

		<div v-else class="like-comment">
			<button
			class="btn"
			@click="toggleLike"
			:class="{
				'btn-danger': userLikedComment,
				'btn-outline-danger': !userLikedComment,
			}"
			>
				<strong>{{ likesNumber }} Mi piace </strong>
			</button>
		</div>
	</div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
	name: "CommentComponent",
	props: {
		comment:{
			type: Object,
			required: true
		},
		requestUser:{
			type: String,
			required: true
		}
	},
	data(){
		return{
			userLikedComment: this.comment.user_has_voted,
			likesNumber: this.comment.likes_count
		}
	},
	computed:{
		isCommentAuthor(){
			return this.comment.author === this.requestUser
		}
	},

	methods:{
		triggerDeleteComment(){
			this.$emit("delete-comment", this.comment)
	},
	
		toggleLike(){
			this.userLikedComment === false 
				? this.likeComment() 
				: this.unLikeComment()
	},
		likeComment(){
			this.userLikedComment = true;
			this.likesNumber += 1;
			let endpoint =  `/api/comments/${this.comment.id}/like/`;
			apiService(endpoint, "POST");
			//non effettuiamo ulteriori controlli perchè sono dati innocui, stessa cosa per unLikeComment. Cosi è piu veloce
	},
		unLikeComment(){
			this.userLikedComment = false;
			this.likesNumber -= 1;
			let endpoint =  `/api/comments/${this.comment.id}/like/`;
			apiService(endpoint, "DELETE");
			
	}

}
}
</script>


<style lang="css">

</style>