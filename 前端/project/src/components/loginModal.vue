<template>
    <div class="login-modal" v-show="$store.state.login.show">
    <div class="login-modal_content">
      <div class="login-modal_hd">
          <h3>登录</h3>
          <button class="close" @click="turnOffLoginModal">×</button>
      </div>
      <div class="login-modal_bd">
        <div role="form" class="login-modal_form">
            <div class="form-group">
                <label class="control-label">Email</label>
                <input class="form-control" v-model="userEmail" type="text" name="userName" placeholder="请输入Email"/>
            </div>
             <div class="form-group">
                <label class="control-label">密码</label>
                <input class="form-control" type="password" name="userPwd" v-model="userPwd" placeholder="请输入密码"/>
            </div>
             <div class="form-group">
                <button  class="form-control login-btn" @click="check">登录</button>
            </div>
        </div>
      </div>
    </div>
   </div>
</template>
<script>
import { mapMutations, mappGetters, mapActions } from "vuex";
import fetch from '../fetch.js'
export default {
  name: "app",
  components:{
        fetch
  },
  data(){
      return{
          userEmail:"",
          userPwd:"",
      }
  },
  methods: {
    ...mapMutations({
      turnOnLoginModal: "turnOnLoginModal",
      turnOffLoginModal: "turnOffLoginModal",
      update:"update"
    }),
    check(){
        $.ajax({
          type:"post",
<<<<<<< HEAD:Demo/diary/project/src/components/loginModal.vue
          url:this.$store.state.ip.url1+"/login",
=======
          url:"http://59.77.134.23:5000/login",
>>>>>>> 450ead2ae1643020664b7cceb06a28963b55830e:Demo/src/components/loginModal.vue
          dataType:"json",
          data:{
            "userEmail":this.userEmail,
            "userPwd":this.userPwd
          },
          success:(data)=>{
            console.log(data)
              if(data.status){
                fetch.storage.set('token',data.token)
                fetch.storage.set('isLogin',true)
<<<<<<< HEAD:Demo/diary/project/src/components/loginModal.vue
                console.log(data.userName)
               fetch.storage.set('userName',data.userName)
               fetch.storage.set('userId',data.userId)
=======
>>>>>>> 450ead2ae1643020664b7cceb06a28963b55830e:Demo/src/components/loginModal.vue
                this.turnOffLoginModal();
                this.update()
              }
              else{
                alert("邮箱或密码错误！")
              }
          },
          error:function(error){
            console.log(error)
          }
        })
    }
  },
  mounted(){

  }
};
</script>
<style>
/*登陆弹出框*/
.login-modal {
  height: 100%;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 100;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}
.login-modal_content {
  width: 400px;
  background-color: #fff;
  position: absolute;
  left: 0;
  top: 200px;
  right: 0;
  margin: auto;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  border-radius: 5px;
  -webkit-animation-name: animatetop;
  -webkit-animation-duration: 0.2s;
  animation-name: animatetop;
  animation-duration: 0.2s;
}
.login-modal_hd {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background-color: #f3f3f3;
  height: 30px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
}
.login-modal_bd {
  display: flex;
  justify-content: center;
  padding: 20px 0 50px 0;
}
.close {
  border: none;
  background-color: #f3f3f3;
  cursor: pointer;
  font-weight: 700;
  font-size: 140%;
  outline: none;
  color: #c2c2c2;
}
.control-label {
  display: block;
  font-weight: 700;
}
.form-control {
  width: 250px;
  height: 10px;
  padding: 11px 10px;
  margin-bottom: 20px;
  border-radius: 2px;
  border: 1px solid #dbdbdb;
}
.login-btn {
  background-color: #3582f8;
  cursor: pointer;
  color: #ffffff;
  font-family: Microsoft YaHei, SimHei, Tahoma;
  border: none;
  height: 41px;
  border-radius: 4px;
}
@-webkit-keyframes animatetop {
  from {
    top: -300px;
    opacity: 0;
  }
  to {
    top: 0;
    opacity: 1;
  }
}

@keyframes animatetop {
  from {
    top: -300px;
    opacity: 0;
  }
  to {
    top: 200px;
    opacity: 1;
  }
}
</style>


