<template lang="html">
	<div class="container">
		<div class="row">
			<div class="col-12">
				<h3 class="my-3">Modifica Commento</h3>
				<form @submit.prevent="onSubmit">
					
					<textarea
					v-model="commentBody" 
					rows="3" 
					class="form-control">	
					</textarea>

					<br>
					<button type="submit" class="btn btn-dark">Conferma Modifica</button>
				</form>
				<p class="error mt-2">{{ error }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default{
	name: "CommentEditor",
	props:{
		id:{
			type: Number,
			required: true
		},
		commentEdit:{
			type:String,
			required: true
		},
		article_slug:{
			type: String,
			required: true
		}

	},

	async beforeRouteEnter(to, from, next){
		let endpoint = `/api/comments/${to.params.id}/`
		await apiService(endpoint)
				.then(data => {
					to.params.commentEdit = data.comment;
					to.params.article_slug = data.article_slug;
				})
		return next();
	},

	data(){
		return{
			commentBody: this.commentEdit, //facciamo questo perchè
											//non è consigliato modificare i prop direttamente
			error: null
			}
	},
	methods:{
		onSubmit(){
			if(this.commentBody){
				let endpoint = `/api/comments/${this.id}/`;
				apiService(endpoint, "PUT", {comment: this.commentBody})
					.then(() => {
						this.$router.push({
							name: "Article",
							params: {slug: this.article_slug}
						})
					})

			}else{
				this.error = "Il campo testuale non può essere vuoto"
			}
		}
	}
	//methods:{
	//	async getCommentData(){
	//		let endpoint = `/api/comments/${this.id}/`
	//		await apiService(endpoint)
	//			.then(data => {
	//				this.commentBody = data.comment;
	//			})
	//	}
	//},
	//created(){
	//	this.getCommentData();
	//}
}
</script>


<style lang="css">
	
</style>