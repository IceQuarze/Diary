<template>
  <div id="app">
    <!--<p>{{$store.state.main_content_data.data}}</p>
    <button @click="$store.dispatch('fetchData')">btn</button>
    <button @click="fetch">btn1</button>-->
    <SideBar></SideBar>
    <Content></Content>
  </div>
</template>

<script>
import SideBar from "./components/sidebar.vue"
import Content from "./components/Content.vue"
import demo from "./components/demo.vue"
import {mapMutations,mapGetters,mapActions} from 'vuex'
export default {
  name: 'App',
  components:{
    SideBar,
    Content,
    demo
  },
  methods:{
    ...mapActions({
     
  })
  },
  created:function(){
     
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100%;
  width: 100%;
}
</style>
