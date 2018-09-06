<template>
<div class="header">
        <div class="container">
           <a class="logo">药丸日记</a>
            <ul class="nav-tab-list">
                <li class="nav-tab-list-item"><a href="index.html">首页</a></li>
                <li class="nav-tab-list-item"><a href="#">话题</a></li>
            </ul>
            <ul class="nav-user-list">
                <li  class="nav-user-list-item" 
                @click="turnOnLoginModal" 
                v-show="!$store.state.login.isLogin"><a>登录</a></li>
                <li class="nav-user-list-item" v-show="!$store.state.login.isLogin"><a href="register.html">注册</a></li>
                <li class="nav-user-list-item" v-show="$store.state.login.isLogin"><a href="write_diary.html">写日记</a></li>
                <li class="nav-user-list-item" 
                v-bind:class="{dropdown:isDropMenu}" 
                @mouseover="showMenu" 
                @mouseout="hideMenu" 
                v-show="$store.state.login.isLogin">
                  <a >{{$store.state.login.userName}}</a>
                  <span class="caret"></span>
                  <ul class="user" v-show="isshow">
                      <li><a href="myDiary.html">我的日记</a></li>
                      <li><a href="createDiary.html">创建日记本</a></li>
                      <li><a href="user.html">个人中心</a></li>
                      <li @click="logout"><a >退出</a></li>
                  </ul>
                </li>
            </ul>
        </div>
</div>  
</template>
<script>
import { mapMutations, mappGetters, mapActions } from "vuex";
import fetch from '../fetch.js'
export default {
  data(){
    return{
      isshow:false,
      isDropMenu:false,
    
    }
  },
  computed:{
    isLogin(){
      return fetch.storage.get('isLogin')
    }
  },
  methods: {
    ...mapMutations({
      turnOnLoginModal: "turnOnLoginModal",
      turnOffLoginModal: "turnOffLoginModal",
      update:"update"
    }),
    showMenu(){
      this.isDropMenu=true;
        this.isshow=true;
    },
    hideMenu(){
      this.isDropMenu=false;
      this.isshow=false;
    },
    logout(){
      fetch.storage.set("isLogin",false)
      this.update()
      window.location.href="index.html"
    }
  }
};
</script>

<style>
.container a{
    text-decoration: none;
    color: #74799b;
}
.container a:hover{
    color: #000;
}
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: #f8f8f8;
  z-index: 10;
  box-shadow: 0 0 5px #ccc;
}
.container {
  width: 960px;
  margin: 0 auto;
}
.container li {
  cursor: pointer;
}
.container .logo {
  float: left;
  background: url(../image/logo.png) no-repeat;
  background-size: contain;
  height: 40px;
  width: 80px;
  padding-left: 50px;
  line-height: 40px;
}
.nav-tab-list {
  list-style: none;
  float: left;
  line-height: 40px;
}
.nav-tab-list-item {
  display: block;
  float: left;
  margin-left: 20px;
}
.nav-user-list {
  list-style: none;
  line-height: 40px;
  float: right;
}
.nav-user-list-item {
  float: left;
  display: block;
  margin-right: 20px;
  font-weight: bold;
  color: #423e3d;
}
.dropdown{
  position: relative;
  background-color:#fff; 
   box-shadow: 0 0 5px #ccc;
}
.user{
  position: absolute;
  right: 0;
  list-style: none;
  background-color:#fff; 
  width: 100px;
  text-align: right;
 
}
.user li{
  width: 100%;
  font-weight: 300;
  height: 30px;
  color: #000;
  font-size: 14px;
  line-height: 30px; 
}
.user li:hover{
  color: #fff;
  background-color: #359aee;
}
.user  a{
  color: #000;
  padding-right:10px; 
}
.caret {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #666;
    content: "";
    display: inline-block;
    height: 0;
    vertical-align: top;
    width: 0;
    margin-top: 18px;
}
</style>

