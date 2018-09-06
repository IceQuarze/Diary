<template>
  <div id="app">
      <Nav></Nav>
      <LoginModal></LoginModal>
      <div class="page">
        <div class="diary-info">
            <h3>创建日记本</h3>
            <div class="diary-info-form">
                <div class="form-group">
                    <label class="label-txt">主题</label>
                    <input class="form-control" name="subject" v-model="subject" /> 
                </div>
                <div class="form-group">
                    <label class="label-txt ">简单的介绍:</label>
                    <textarea name="decription"  class="decription" v-model="decription"></textarea>
                </div>
                <div class="form-group">
                  <label class="label-txt">谁可以看我的日记</label>
                  <select class="privacy" name="privacy">
                      <option>公开</option>
                      <option>自己</option>
                  </select>
                </div>
                <div class="form-group">
                      <label class="label-txt">结束时间</label>
                      <input type="date"  name="endTime" id="endTime" class="form-control"/>
                </div>
                <div class="form-group">
                     <button type="button" @click="check" class="create-diary-btn">创建</button>
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
import fetch from "../../fetch.js"
export default{
  name:'App',
  components:{
    Nav,
    LoginModal
  },
  data:function(){
    return {
      subject:"",
      decription:"",
      islock:false
    }
  },
  methods:{
      check:function(){
        if(this.subject==""){
          alert("主题不能为空!")
        }
        else{
            if(this.islock)return;
            this.islock=true;
            var endTime=document.getElementById("endTime");
            endTime=endTime.value
            endTime=new Date(endTime).getTime();
            var privacy=document.getElementsByClassName("privacy")[0].nodeValue;
            var uri=this.$store.state.ip.url2+"/book.php";
            $.ajax({
              type:"post",
              url:uri,
              data:{
                "op":"post",
                "subject":this.subject,
                "description":this.decription,
                "endTime":endTime/1000,
                "privacy":privacy,
                "token":"" + fetch.storage.get('token'),
              },
              success:function(data){
                data=JSON.parse(data)
                console.log(data.status)
                        
                if(data.status){
                  window.location.href="write_diary.html"
                }
                
              },
              error:function(error){
                console.log(error)
              }
            }),
            setTimeout(()=>{
                this.islock=false;
            },3000)
                     
        }
      }
  },
  mounted:function(){
        var M=[31,28,31,30,31,30,31,31,30,31,30,31];
        var endTime=document.getElementById("endTime");
        var now=new Date();
        var day=now.getDate();
        var month=now.getMonth();
        var year=now.getFullYear();
        if(year%4==0&&year%100!=0||year%400==0)M[1]=29;
        day+=30;
        while(day>M[month]){
          day-=M[month];
          if(month==11)year++;
          month++;
        }
        var def=new  Date(year,month,day);
        console.log(def)
        endTime.valueAsDate=def;
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
.diary-info{
  margin-top:60px; 
}
.diary-info h3{
  margin-bottom:20px; 
}
.label-txt{
  display: block;
  margin: 20px 0 0 5px 0;
}
.decription{
  height: 100px;
  width: 250px;
  padding: 11px 10px;
  margin-bottom:15px; 
}
.privacy{
  padding: 11px 10px;
  height: 40px;
  width: 270px;
  margin-bottom:15px; 
}
.create-diary-btn{
  border: none;
  background-color: #3582f8;
  cursor: pointer;
  color: #ffffff;
  font-family: Microsoft YaHei, SimHei, Tahoma;
  height: 31px;
  border-radius: 4px;
  width: 50px;
}
.create-diary-btn:hover{
  background-color: #5d9bf9;
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
</style>
