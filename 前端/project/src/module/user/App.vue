<template>
  <div id="app">
      <Nav></Nav>
      <LoginModal></LoginModal>
      <div class="page">
        <div class="main_content">
             <div class="form-group">
                <label class="control-label">昵称</label>
                <input class="form-control" v-model="userName"  placeholder="请输入要更改的昵称"/>
            </div>
            <div class="form-group">
            <label class="control-label">头像</label>
            <input type="file" class="diary-photo form-control" id="head-img" name="diaryImg">
            </div>
            <input type="txt" class="diary-photo-input form-control" placeholder="点击上传照片...">
             <button  class="userInfo-submit-btn" @click="submitInfo">上传</button>
        </div>
      </div>
  </div>
</template>

<script>
import LoginModal from '../../components/loginModal.vue'
import Nav from "../../components/nav.vue"
export default{
  name:'app',
  data(){
    return {
      userName:""
    }
  },
  components:{
    Nav,
    LoginModal
  },
  methods:{
    submitInfo:function(){
      var headImg=document.getElementById("head-img").value;
      $.ajax({
        type:"post",
        dataType:"json",
        url:"",
        data:{
          "userName":this.userName,
          "headImg":headImg,
        },
        success:function(data){
            console.log(data)
        },
        error:function(error){
          
        }
      })
    }
  }
}
</script>
<style>
#app {
  width: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
 
}
.page{
  width: 960px;
  margin: 0 auto;
}
.main_content{
  display: flex;
  flex-direction: column;
  margin-top: 80px; 
}
.diary-photo{
  height: 42px;
  margin: 8px 0;
  opacity: 0;
}
.diary-photo-input{
  height: 20px;
  margin-top:-48px; 
  padding: 11px 10px;
  z-index: -1;
  margin-bottom:8px; 
}
.userInfo-submit-btn{
   width: 80px;
  margin-top:10px;
  border: none;
  height: 30px;
  border-radius:3px;
  background-color: #1d4fd4;  
  color: #fff;
}
</style>
