import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Article from "../views/Article.vue";
import ArticleEditor from "../views/ArticleEditor.vue";
import CommentEditor from "../views/CommentEditor.vue";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/article/:slug",
    name: "Article",
    component: Article,
    props:true
  },

  {
    path: "/create-article/:slug?", //il ? indica che il paramentro è opzionale
    name: "article-editor",
    component: ArticleEditor,
    props: true
  },
  {
    path: "/comment/:id",
    name: "comment-editor",
    component: CommentEditor,
    props: true
  },
  {
    path: "*",
    name: "page-not-found",
    component: NotFound
  },
  
];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL, commentato per rimuovere doppio url
  routes
});

export default router;
