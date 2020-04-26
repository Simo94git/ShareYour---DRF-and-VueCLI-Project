<template lang="html">
		
	<nav class="NavBarStile navbar navbar-expand navbar-light bg-light">
	<div class="container">
		
		 <router-link 
			  :to="{ name: 'Home' }" 
			  class="navbar-brand">ShareYourWords
		</router-link>
		 
			<li><span style="font-style: italic;">progetto dimostrativo creato da </span> <a href="https://github.com/Simo94git">Simo94git</a></li>
		  <div class="collapse navbar-collapse" id="navbarSupportedContent">
		    <ul class="navbar-nav ml-auto">
		      	<li class="nav-item">
		      		<router-link 
			  			:to="{ name: 'Home' }" 
			 			class="btn btn-dark">Home
					</router-link></li>
		      	<li class="nav-item mx-1">
		      		<router-link 
			  			:to="{ name: 'article-editor' }" 
			 			class="btn btn-dark">Scrivi
					</router-link></li>
		    	

				<li>
					<a 
					class="btn btn-danger" 
					href="/accounts/logout/">
						Logout
					</a>
				</li>
		      	

		    </ul>
		    
		  </div>

	 </div>
	</nav>


</template>

<script>
	export default {
		name: "NavbarComponent"
	}
</script>

<style lang="css">
	.NavBarStile {
		border-bottom: 1px solid #DDD;
		background-color: #bfbab7;
	}
	.navbar-brand {
		font-weight: bold;
		font-size: 150%;
	}

	.navbar-brand:hover {
		color: #DC3545 !important;
	}

</style>