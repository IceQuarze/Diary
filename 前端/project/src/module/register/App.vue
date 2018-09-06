<template>
  <div id="app">
    <Nav></Nav>
      <div class="page">
       <form  class="form" >
        <div class="form-group">
          <label class="form-group_txt">用户名 </label>          
          <input class="user-name input-default" name="userName" v-model="userName" type="text" placeholder="请设置用户名"/>
        </div>
        <div class="form-group">  
          <label class="form-group_txt">电子邮箱 </label>          
          <input class="user-email input-default" type="text" v-model="userEmail" @blur="checkEmail" name="userEmail" placeholder="请输入您的邮箱"/>
           <span class="tips">{{email_tips}}</span> 
        </div>
        <div class="form-group">
          <label class="form-group_txt">密码 </label>          
          <input class="user-password input-default" type="password" v-model="userPwd" name="userPwd" placeholder="请设置密码"/>
         
        </div> 
        <div class="form-group"> 
          <label class="form-group_txt" >确认密码 </label>          
          <input class="ensure-password input-default" @blur="checkPwd" v-model="ensureUserPwd" type="password" name="ensureUserPwd" placeholder="请确认您的密码"/>
          <span class="tips">{{pwd_tips}}</span>
        </div>
        <div class="form-group">
           <input type="button" @click="check" id="register-btn" class="register-btn input-default" value="注册"/>
        </div>
      </form>
      </div>
      <div class="footer">
        <div class="copy-box">2018&nbsp;©Diary</div>
      </div>
      <LoginModal></LoginModal>
  </div>
</template>

<script>
import LoginModal from '../../components/loginModal.vue'
import Nav from "../../components/nav.vue"
export default{
  name:'app',
  data:function(){
      return {
        userName:"",
        userEmail:"",
        userPwd:"",
        ensureUserPwd:"",
        email_flag:false,
        pwd_flag:false,
        email_tips:"",
        pwd_tips:""
      }
  },
  components:{
    Nav,
    LoginModal
  },
  methods:{
    check:function(){
      var btn=document.getElementById("register-btn");
      if(this.pwd_flag&&this.email_flag&&this.userName){
        $.ajax({
          type:"post",
          url:this.$store.state.ip.url1+"/register",
          dataType:"json",
          data:{
              "userName":this.userName,
              "userEmail":this.userEmail,
              "userPwd":this.userPwd
          },
          success:function(data){
            console.log(data)
              if(data.status){
                alert("注册成功");
                window.location.href="./index.html"
              }
              else {
                alert("邮箱已被注册")
                this.userPwd="";
                this.ensureUserPwd="";
                this.userEmail="";
              }
          },
          error:function(error){
              console.log(error)
          }
        })
      }
    },
    checkEmail:function(){
      var reg=/^[a-zA-Z0-9]+@([a-zA-Z0-9]+\.)+(com|cn|net|edu)$/;
      if(reg.test(this.userEmail)){
          this.email_flag=true
          this.email_tips="";
      }
      else{
          this.email_flag=false;
          this.email_tips="* 邮箱格式错误"
      }
    },
    checkPwd:function(){
      if(this.userPwd==this.ensureUserPwd){
        this.pwd_flag=true;
        this.pwd_tips=""
      }
      else {
          this.pwd_flag=false;
          this.pwd_tips="* 两次输入密码不一致"
      }    
    }
  }
}
</script>
<style>
*{
  margin: 0;
  padding: 0;
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
  margin-top:100px;
  margin-bottom:80px; 
}
.form{
  display: flex;
  height: 300px;
  flex-direction:column;
  justify-content: space-around; 
}
.form-group{
  width: 100%;
}
.form-group_txt{
  display: block;
  width: 80px;
  float: left;
  text-align: right;
  color: #666;
  font-weight:700;
  height:42px;
  line-height: 42px; 
}
.input-default{
  display: block;
  float: left;
  height: 16px;
  padding: 11px 10px;
  margin-left: 13px;
  width:300px;
  font-size:14px;
  color: #666 ;
}
.register-btn{
  height: 45px;
  font-weight: 700;
  cursor: pointer;
  color:#fff;
  border: none;
  background-color: #3f89ec;
  border-radius: 3px;
  margin-left:90px;
  width: 324px; 
}
.footer{
  display: flex;
  justify-content: center;
  align-items: center;
}
.tips{
  line-height: 42px;
  margin-left:20px;
  color: #fc4343; 
}
</style>
