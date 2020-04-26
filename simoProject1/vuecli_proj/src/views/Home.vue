<template>
  <div class="home">
  	<div class="container cont mt-4">
  		 <div class="mt-2">
         <div v-for="(x , index) in articles" :key="index" >

          <h2><router-link 
              :to="{name: 'Article', params: { slug: x.slug } }"
              class="article_link">
              {{ x.title }}
            </router-link></h2>

           <p class="art">Articolo aggiunto da <span class="author-name"><strong>{{ x.author }}</strong></span></p>
           <br>
            <div class="DivTextLimited">
              {{ x.content }}
            </div>
            <br>
           <p class="commentStyle">Commenti: <span>{{ x.comments_count }}</span></p>
           
            


          
           <hr>
         </div>
                  <div class="my-4">
                    <p v-show="loadingArticles">loading...</p>
                    <button v-show="next"
                            @click="getArticles"
                            class="btn btn-dark mt-0">carica ancora</button>
        </div>
       </div>
  	</div>
  </div>

</template>

<script>
import { apiService } from "../common/api.service.js"



export default {
  name: "Home",
  data(){
    return{
      articles: [],
      next: null,
      loadingArticles: false
    }
  },

  methods: {

    getArticles(){
      let endpoint = "api/articles/";
      if(this.next){
        endpoint = this.next; 
      }
      this.loadingArticles = true;

      apiService(endpoint)
        .then(data => {
        this.articles.push(...data.results);

        this.loadingArticles = false;
        if(data.next){
          this.next = data.next;
        }else{
          this.next = null;
        }
      })
    }
  },

  created(){
    this.getArticles();
    document.title = "ShareYour";
  }

  
};
</script>

<style>
  .author-name{
    font-weight: bold;
    color: red;
  }
  .article_link{
    font-weight: bold;
    color: black;
  }

  .article_link:hover{
    color: #343A40;
    text-decoration: none;

  }
  .cont{
  font-size: 120%;
 }
 .commentStyle{
  margin-top: -5px
 }
 .art{
  margin-bottom: -0px;
 }

 .DivTextLimited{
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
 }
</style>
