<template lang="html">
	<div class="article-actions">

		<router-link 
		:to="{name: 'article-editor', params: {slug: slug } }"
		class="btn btn-secondary mr-1">
			<span>Modifica</span>
		</router-link>

		<button class="btn btn-danger"
				@click="deleteArticle">
			Cancella
		</button>

	</div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default{
	name: "ArticleActions",
	props:{
		slug:{
			type: String,
			required:true
		}
	},
	methods:{
		async deleteArticle(){
			let endpoint =  `/api/articles/${this.slug}/`;
			try{
				await apiService(endpoint, "DELETE");
				this.$router.push("/")
			}catch(err){
				console.log(err)
			}
		}
	}

}
</script>

<style lang="css">
	
</style>