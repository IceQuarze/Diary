<template>
  <div id="app">
      <Nav></Nav>
      <LoginModal></LoginModal>
      <Loading v-show="$store.state.myDiaryData.show"></Loading>
     <div class="page">
       <div class="main_content">
         <div class="diary-header">
           <h3>{{userName}}的日记本</h3>
           <a class="creat-diary" href="createDiary.html">创建日记本</a>
         </div>
      <div class="myDiary-box">
        <div class="myDiary"  v-for="item in $store.state.myDiaryData.data" @click="showDiary($event)" :data-bookid="item.bookId">
          <img src="./image/diary-icon.png" :data-bookid="item.bookId">
          <p class="diary-title" v-bind:title="item.description" :data-bookid="item.bookId">{{item.bookName}}</p>
          <div class="diary-time" :data-bookid="item.bookId">
          <p class="diary-begin-time" :data-bookid="item.bookId">{{item.beginTime}}创建</p>
          <p class="diary-end-time" :data-bookid="item.bookId">{{item.endTime}}结束</p>
        </div>
        </div>
      </div>
      </div>
      <div class="sideBar">
          <div class="user-info">
              <img :src="headImage"/>
              <p>{{userName}}</p>
          </div>
      </div>
     </div>
  </div>
</template>

<script>
import Loading from '../../components/Loading.vue'
import LoginModal from '../../components/loginModal.vue'
import Nav from "../../components/nav.vue"
import { mapMutations, mappGetters, mapActions } from "vuex";
import fetch from '../../fetch';
export default{
  name:'App',
  components:{
    Nav,
    LoginModal,
    Loading
  },
  data:function(){
    return{
        headImage:"",
        userName:fetch.storage.get('userName')
    }
  },
  methods:{
    ...mapMutations({
      getMyDiaryData:"getMyDiaryData"
    }),
    showDiary:function(e){
        console.log(e)
        var bookId=e.target.getAttribute('data-bookId');
        console.log(bookId)
        fetch.storage.set('bookId',bookId);
        window.location.href="noteBook.html"
    }
  },
  created(){
    var userId=fetch.storage.get("userId");
    console.log(userId)
    this.getMyDiaryData();
    $.ajax({
      type:"post",
      url:this.$store.state.ip.url1+"/get_user_info_js",
      dataType:"json",
      data:{
        "userId":userId
      },
      success:(data)=>{
          console.log(data);
          this.headImage=data.headImageURL
      },
      error:function(e){
        console.log(e)
      }
    })
  },
  


}
</script>
<style>
*{
  padding: 0;
  margin: 0;
  font-family: Microsoft YaHei, SimHei, Tahoma;
}
html,body{
  height: 100%;
  width: 100%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
 
}
.page{ 
  width: 960px;
  margin: 0 auto;  
}
.diary-header{
  display: flex;
  margin-left: 5%;
  margin-bottom:20px; 
}
.creat-diary{
  border: noD;
  background-color: #3582f8;
  color: #fff;
  padding: 3px 8px;
  display: block;
  margin-left:15px;
  cursor: pointer; 
  border-radius: 2px;
  text-decoration: none;
  font-size: 12px;
}
.creat-diary:hover{
  background-color: #5d9bf9;
}
/*日记本九宫格*/
.main_content{
  float: left;
  width: 60%;
  padding-right:10%; 
  background-color: #ffffff;
  margin-top:100px; 
  border-right: 1px dashed #ccc;  
}
.myDiary-box{
  width: 100%;
  display: flex;
  flex-wrap:wrap;
  justify-content: flex-start;
}
.myDiary{
  width: 30%;
  position: relative;
  cursor: pointer;
  margin-right:3%; 
}
.myDiary:hover{
  color: #74799b;
  box-shadow: 0 0 5px #ccc; 
}
.myDiary img{
  width: 100%;
}
.diary-title{
  position: absolute;
  left: 30%;
  font-size: 10px;
  top: 20%;
  padding: 5px;
  width: 70px;
  height: 20px;
  background-color: #d0d0d0;
  overflow: hidden;
}
.diary-time{
  position: absolute;
  bottom: 20%;
  left: 33%;
  font-size: 10px;
  color: #9c9f9f;
}
/*侧边栏*/
.sideBar{
  float: right;
  background-color: #fff;
  width: 28%;
  float: right;
  margin-top:100px;
}
.user-info{
  margin-top: 20px;
}
.user-info img{
  margin-bottom: 15px;
  height: 100px;
  width: 100px;
  border-radius:5px; 
}
.user-info p{
  font-size: 150%;
}
</style>
