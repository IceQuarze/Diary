<template>
  <div id="app">
      <Nav></Nav>
      <LoginModal></LoginModal>
      <div class="page">
              <div class="main_content">
                  <h3>《{{bookName}}》</h3>
                  <div class="diaryContent">
                      <div class="diaryContent-item" v-for="item in data">
                         <p>{{item.createTime}}：    {{item.diaryContent}}</p>
                          <img :src="item.diaryImg" class="photo">
                      </div>
                  </div>
              </div>
      </div>
      <div class="page-footer">
        <div class="copy-box">2018&nbsp;©Diary</div>
      </div>
  </div>
</template>

<script>
import LoginModal from '../../components/loginModal.vue'
import Nav from "../../components/nav.vue"
import fetch from '../../fetch.js'
export default{
  name:'app',
  components:{
    Nav,
    LoginModal
  },
  data(){
    return{
      data:[],
      bookName:"",
    }
  },
  mounted(){
    var token=fetch.storage.get("token")
    var bookId=fetch.storage.get("bookId")
    console.log(token)
    console.log(bookId)
    $.ajax({
      type:"post",
      dataType:"json",
      url:this.$store.state.ip.url2+"/diary.php",
      data:{
          "token":token,
          "op":"get",
          "bookId":bookId
      },
      success:(data)=>{
          console.log(data)
          var _this=this;
           data.diaryList.forEach(element => {
            var date = new Date(parseInt(element.createTime)*1000);
            var Y = date.getFullYear() + '-';
            var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
            var D = date.getDate() +' ';
            var h = date.getHours() + ':';
            var m = date.getMinutes() + ':';
            var s = date.getSeconds();
            element.createTime=Y+M+D+h+m+s;
            _this.data.push(element)
           });
            this.bookName=data.bookName
      },
      error:function(e){
        console.log(e.responseText)
      }
    })
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
  margin-top:80px; 
  width: 65%;
}
.diaryContent{
  margin-top:20px;
  padding: 30px 11px 10px 11px;
  border-top: 1px dotted #000;
  border-bottom: 1px dotted #000;
}
.diaryContent-item{
  padding: 10px 11px;
  margin-bottom: 20px; 
  border-radius:5px;
  background-color:rgba(100, 220, 230, 0.1);  
  box-shadow: 0 0 5px #ccc;
}
.page-footer {
  border-top: 1px solid #d5d5d5;
  margin-top: 50px;
  padding-top: 30px;
  padding-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.photo{
  width: 150px;
  height: auto;
  cursor: pointer;  
}
</style>
