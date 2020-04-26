<template lang="html">
	<div class="container">
		<div class="row">
			<div class="col-12">
				<h1 class="mb-3">Scrivi un articolo</h1>
				<form @submit.prevent="onSubmit">
					
					<textarea 
					v-model="article_title" 
					rows="1" 
					class="form-control"
					placeholder="Titolo dell'articolo">
					</textarea>
					<br>
					<textarea 
					v-model="article_body" 
					rows="10" 
					cols="30"
					class="form-control"
					placeholder="...">
						
					</textarea>
					<br>
					<button type="submit" class="btn btn-dark">Pubblica il tuo articolo</button>
				</form>
				<p class="muted error mt-2">{{ error }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default{
	name: "ArticleEditor",

	props: {
		slug:{
			type: String,
			required: false //false perchè ci serve solo il contenuto
		},
		previousArticle:{
			type: String,
			required: false
		},
		previousArticleContent:{
			type: String,
			required: false
		}

	},

	data(){
		return {
			article_title: this.previousArticle || null,
			article_body: this.previousArticleContent || null,
			
			error: null
		}
	},

	async beforeRouteEnter(to, from, next){
		if(to.params.slug !== undefined){
			let endpoint = `/api/articles/${to.params.slug}/`;
			await apiService(endpoint)
				.then((data) => {
					to.params.previousArticle = data.title;
					to.params.previousArticleContent = data.content;
				})
		}
		return next();
	},

	methods:{
		onSubmit(){
			if (!this.article_body || !this.article_title){
				this.error = "Scrivi qualcosa prima di pubblicare l'articolo"	
			}else if(this.article_title.length>240){
				this.error = "Il titolo non può superare i 240 caratteri"
			}else{
				let endpoint = "/api/articles/";
				let method = "POST";
				if(this.previousArticle || this.previousArticleContent){
					method = "PUT";
					endpoint += `${this.slug}/`;
				}
				apiService(endpoint, method, {title: this.article_title,
											  content: this.article_body})
					.then(article_data =>{
						this.$router.push({
							name: "Article",
							params: {slug:article_data.slug}
						})
					})
			}
		}
	},

	created(){
		document.title = "Editor - ShareYour";
	}
}
</script>

<style lang="css">
	
</style>

