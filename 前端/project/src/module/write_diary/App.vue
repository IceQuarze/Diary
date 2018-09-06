<template>
  <div id="app">
      <Nav></Nav>
      <div class="main_content">
        <div  class="write-diary-section">
            <h1 class="tip">日记</h1>
            <select class="diary-title" name="diaryName">
              <option v-for="item in diaryName" v-bind:data-bookId="item.bookId">{{item.bookName}}</option>
              
            </select>
            <input type="file" class="diary-photo" @change="imgChange($event)" name="diaryImg" accept=".gif,.jpg,.jpeg,.png">
            <input type="txt" class="diary-photo-input" placeholder="点击上传照片...">
            <textarea class="diary-content" name="diaryContent"></textarea>
            <button  class="diary-submit-btn"
            @click="check">发布日记</button>
        </div>        
      </div>
      <div class="footer">
        <div class="copy-box">2018&nbsp;©Diary</div>
      </div>
      <LoginModal></LoginModal>
      <Loading v-show="isshow"></Loading>
  </div>
</template>

<script>
import Loading from '../../components/Loading.vue'
import fetch from "../../fetch.js"
import LoginModal from '../../components/loginModal.vue'
import Nav from "../../components/nav.vue"
export default{
  name:'app',
  data(){
    return {
      diaryName:[],
      isLock:false,
      diaryImg:"",
      isshow:true,
    }
  },
  components:{
    Nav,
    LoginModal,
    Loading
  },
  methods:{
    imgChange:function(e){
     
        var diaryImg=document.getElementsByClassName("diary-photo")[0].value;
        
        var reader=new FileReader();
        var _this=this;
        reader.onload=(function(file){
          return function(e){
          _this.diaryImg=this.result;

          }
        })(diaryImg)
        reader.readAsDataURL(e.target.files[0]);
    },
    check:function(){
      var Name=document.getElementsByClassName("diary-title")[0].value;
      var diaryContent=document.getElementsByClassName("diary-content")[0].value;
      if(Name==""){
        alert("请先选择日记本");
        return;
      }
      if(this.isLock)return;
      var bookId
      this.diaryName.forEach(function(element) {
        if(element.bookName===Name){
            bookId=element.bookId
        }
      });
    
      this.isLock=true;
      var token=fetch.storage.get("token")
       $.ajax({
        type:"post",
        url:this.$store.state.ip.url2+"/diary.php",
        dataType:"json",
        data:{
          "diaryImg":this.diaryImg,
          "diaryContent":diaryContent,
          "op":"post",
          "token":token,
          "bookId":bookId,
          "bookName":Name
        },
        success:(data)=>{
          console.log(data)
          if(data.status){
            window.location.href="index.html"
          }
          else{
            alert("出现错误")
          }
        },
        error:function(e){
          console.log(e.responseText)
        }
      })
      setTimeout(()=>{
          this.isLock=false;
      },3000)
     
    }
  },
  mounted(){
    var token=fetch.storage.get('token');
     $.ajax({
        type:"post",
        url:this.$store.state.ip.url2+"/book.php",
        dataType:"json",
        data:{
            "token":token,
            "op":"get",
        },
        success:(data)=>{
          console.log(data)
          var _this=this;
          this.isshow=false;
          var i=0;
          while(data[i]){
            _this.diaryName.push(data[i])
            i++;
          }
        },
        error(e){
            console.log(e.responseText)
        }
      })
  }
}
</script>
<style>
*{
  margin: 0;
  padding: 0;
}
#app {
  width: 100%;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.main_content {
  width: 960px;
  margin: 0 auto; 
}
.write-diary-section{
  margin-top:100px; 
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin-bottom:80px; 
}
.diary-title{
  margin: 8px 0;
  height: 42px;
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
.diary-content{
  height: 300px;
  resize: none;
}
.footer{
  display: flex;
  justify-content: center;
  align-items: center;
}
.diary-submit-btn{
  width: 80px;
  margin-top:10px;
  border: none;
  height: 30px;
  border-radius:3px;
  background-color: #1d4fd4;  
  color: #fff;
  cursor: pointer;
}
</style>
