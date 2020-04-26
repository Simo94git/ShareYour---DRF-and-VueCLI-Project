<template>
  <div class="single-article mt-3">

  <div v-if="notFound" class="container">
    <h1 class="notFound">Domanda non trovata</h1>
  </div>

  	<div  v-else class="container">
      <p class="mb-0">Articolo aggiunto da 
            <span class="author-name"><strong>{{ article.author }}</strong></span></p>
            <br>
      <h2>{{ article.title }}</h2>

      <div style="white-space: pre-line; word-break: break-word; text-align: justify ;">
        {{ article.content}}
      </div>
      
      <div class="row">
         <div class="ml-auto my-0">
          <p style="font-size: 85%;">scritto in data: <strong>{{ article.created_at }}</strong></p> 
      </div>
      </div>
     
      
      <p style="font-size: 90%;">Mi piace: <strong>{{ article.likes_count }}</strong></p> 

      <ArticleActions v-if="isOwner" :slug="slug"/>
      <ArticleLike v-if="isNotOwner" :article="article"/>
      <hr>
            <template v-if="userHasCommented">
                <p class="comment-added">Hai commentato questo articolo</p>
            </template>

            <template v-else-if="showForm">
              <form class="card" @submit.prevent="onSubmit">
                <div class="card-header px-3">
                  Scrivi il tuo commento
                </div>
                <div class="card-block">
                  <textarea 
                  class="form-control"
                  rows="5"
                  placeholder="..."
                  v-model="newCommentBody">
                  
                  </textarea>
                </div>

                <div class="card-footer px-3">
                  <button type="submit"
                          class="btn  btn-dark">
                    Aggiungi Commento
                  </button>
                </div>
              </form>
              <p class="text-muted error mt-2">{{ error }}</p>
            </template>

            <template v-else>
                <button class="btn btn-dark"
                        @click="showForm = true">
                  Commenta Articolo
                </button>
            </template>

      <hr>
      <CommentComponent
          v-for="(comment, index) in comments"
          :comment="comment"
          :requestUser="requestUser"
          :key="index"
          @delete-comment="deleteComment"
          />

          <div class="my-4">
            <p v-show="loadingComments">loading...</p>
            <button 
            v-show="next"
            @click="getArticleComments"
            class="btn btn-lg btn-success">
              Carica Ancora
            </button>
          </div>
    </div>
  </div>

   
</template>

<script>
import { apiService } from "../common/api.service.js"
import CommentComponent from "../components/Comment.vue"
import ArticleActions from "../components/ArticleActions.vue"
import ArticleLike from "../components/ArticleLike.vue"


export default {
  name: "Article",

  props:{
    slug: {
      type:String,
      required: true
    }
  },

  components:{
    CommentComponent,
    ArticleActions,
    ArticleLike
  },

  data(){
    return{
      article: {},
      loadingComments: false,
      comments: [],

      userHasCommented: false,
      showForm: false,
      newCommentBody: null,
      error: null,

      next: null,

      requestUser: null

      }
  },

  computed:{
    isOwner(){
      return this.article.author === this.requestUser;
    },
    isNotOwner(){
      return this.article.author !== this.requestUser;
    },
    notFound(){
      return this.article["detail"]
    }
  },

  methods:{

    setPageTitle(title){
      document.title = title;
    },

    setRequestUser(){
      this.requestUser = window.localStorage.getItem("username");
    },

    getArticleData(){
      let endpoint = `/api/articles/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          this.article = data;
          this.userHasCommented = data.user_has_commented;
          this.setPageTitle(data.title)
        })
    
    },

    getArticleComments(){
      let endpoint = `/api/articles/${this.slug}/comments/`;
      if(this.next){
        endpoint = this.next;
      }
      this.loadingComments = true;
      apiService(endpoint)
        .then(data =>{
          this.comments.push(...data.results);
          this.loadingComments = false;
          if(data.next){
          this.next = data.next;
        }else{
          this.next = null;
        }
        })
    },

    onSubmit(){
      if(this.newCommentBody){
        let endpoint = `/api/articles/${this.slug}/comment/`;
        apiService(endpoint, "POST", {comment: this.newCommentBody})
          .then(data => {
            this.comments.unshift(data);
          })
        this.newCommentBody = null;
        this.showForm = false;
        this.userHasCommented = true;
        if(this.error){
          this.error = null;
        }else{
        this.error = "Scrivi qualcosa prima di pubblicare il commento"
      }
    }
  },

  async deleteComment(comment){
    let endpoint = `/api/comments/${comment.id}/`;
    try{
      await apiService(endpoint, "DELETE");
      this.$delete(this.comments, this.comments.indexOf(comment));
      //this.comments.splice(this.comments.indexOf(comment), 1);
      this.userHasCommented = false;
    }
    catch(err){
      console.log(err);
      }
      }
  },

  created(){
    this.getArticleData();
    this.getArticleComments();
    this.setRequestUser();
  }

}


</script>

<style>
 .comment-added{
  color: green;
  font-weight: bold;
 }
 .single-article{
  font-size: 120%;
 }

</style>
