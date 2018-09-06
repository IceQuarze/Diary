<template>
  <div id="app">
      <Nav></Nav>
    <div class="main_content">
    <div class="diary-box" >
  <div class="diary"  v-for="item in page.pageData">
          <div class="diary_hd">
            <a href="#" class="diary_hd-user-head" :style="{backgroundImage: 'url(' + item.userHead + ')', backgroundSize:'contain'}"></a>
            <a href="#" class="diary_hd-user-name">{{item.userName}}</a>
            <label class="diary_hd-time">{{item.createTime}}</label>
            <a href="#" class="diary_hd-book">《{{item.bookName}}》</a>
          </div>
          <div class="diary_bd">
            <p class="diary_bd-content" >{{item.diaryContent}}</p>
            <div v-if="item.diaryImg">
              <img v-show="item.diaryImg" :src="item.diaryImg"  class="diary_bd-photo"/>
            </div>
          </div>
          <div class="diary_ft">
            <a href="#" class="diary_ft-reply">回复</a>
          </div>
      </div>
    </div>
    <!--<div class="SideBar">
    
    </div>-->
    </div>
  <div class="page-number">
    <div class="page-number_bd">
      <a class="page-number-item" @click="prePage"><</a>
      <a class="page-number-item" @click="toThisPage($event)">1</a>
      <a class="page-number-item" @click="toThisPage($event)">2</a>
      <a class="page-number-item" @click="toThisPage($event)">3</a>  
      <a class="page-number-item" @click="nextPage">></a>
    </div>
  </div> 
    <div class="page-footer">
        <div class="copy-box">2018&nbsp;©Diary</div>
    </div>
    <LoginModal></LoginModal>
    <Loading v-show="$store.state.data.show"></Loading>
  </div>
</template>

<script>
import Loading from '../../components/Loading.vue'
import LoginModal from "../../components/loginModal.vue";
import Nav from "../../components/nav.vue";
import { mapMutations, mappGetters, mapActions } from "vuex";
export default {
  name: "app",
  components: {
    Nav,
    LoginModal,
    Loading
  },
  data: function() {
    return {
      data: [],
      page:{
        pageData:[],
        pageCount:5,
        currentPage:1,
      }
    };
  },
  computed:{
    pageSize:function(){
      var size=parseInt(this.data.length/this.page.pageCount);
      if(this.data.length%this.page.pageCount)size++;
      return size
    }
  },
  methods: {
    ...mapMutations({
      turnOnLoginModal: "turnOnLoginModal",
      turnOffLoginModal: "turnOffLoginModal",
      getIndexData: "getIndexData"
    }),
    renderData:function(){
        var start=(this.page.currentPage-1)*this.page.pageCount
        var end=start+this.page.pageCount<this.data.length?start+this.page.pageCount:this.data.length;
        this.page.pageData=[]
        for(var i=start;i<end;++i){
          this.page.pageData.push(this.data[i])
        }
    },
    toThisPage:function(e){
        var lis=document.getElementsByClassName("page-number-item");
        this.page.currentPage=parseInt(e.target.innerText)
        for(var i=1;i<4;++i){
          lis[i].className="page-number-item"
          if(parseInt(lis[i].innerText)==this.page.currentPage){
            lis[i].className+=" page-number-item_active"
          }
        }
       this.scroll()
       this.renderData();
    },
    prePage:function(){
        var lis=document.getElementsByClassName("page-number-item");
        if(parseInt(lis[1].innerText)!=1){
            for(var i=1;i<4;++i){
              lis[i].innerText=parseInt(lis[i].innerText)-1;
            }
        }
        if(this.page.currentPage>1)
          this.page.currentPage--;
        for(var i=1;i<4;++i){
          lis[i].className="page-number-item"
          if(parseInt(lis[i].innerText)==this.page.currentPage){
            lis[i].className+=" page-number-item_active"
          }
        }
       this.scroll()
       this.renderData()
    },
    scroll:function (){
        var currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
        if(currentScroll > 0) {
            window.scrollTo (0,0);
        }
    },
    nextPage:function(){
        var lis=document.getElementsByClassName("page-number-item");
          if(parseInt(lis[3].innerText)!=this.pageSize){
              for(var i=1;i<4;++i){
                lis[i].innerText=parseInt(lis[i].innerText)+1;
              }
          }
          if(this.page.currentPage<this.pageSize)
            this.page.currentPage++;
          for(var i=1;i<4;++i){
            lis[i].className="page-number-item"
            if(parseInt(lis[i].innerText)==this.page.currentPage){
              lis[i].className+=" page-number-item_active"
            }
          }
         this.renderData();
         this.scroll()
    },

    
  },
  mounted: function() {
    this.getIndexData();
    var lis=document.getElementsByClassName("page-number-item");
    this.data = this.$store.state.data.diaryData;
    this.renderData()
    lis[1].className+=" page-number-item_active"
    
  }
};
</script>
<style>
#app {
  font-family: "Lucida Grande", "Lucida Sans Unicode", Helvetica, Arial, Verdana,
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.diary a {
  text-decoration: none;
  font-weight: 600;
  color: #74799b;
}
a:hover {
  text-decoration: underline;
}
/*日记内容*/
.main_content {
  display: flex;
  width: 960px;
  margin: 0 auto;
}
.diary-box {
  width: 72%;
  margin: 80px 0 0 0;
}
.diary {
  box-shadow: 0px 1px 3px rgba(34, 25, 25, 0.2);
  width: 100%;
  padding: 15px;
  background-color: #fff;
  border-radius: 5px;
  margin-bottom: 10px;
}
.diary_hd-user-head {
  display: block;
  float: left;
  height: 50px;
  width: 50px;
  border-radius: 2px;
  background: url(./image/head.jpg);
}
.diary_hd-user-name {
  line-height: 50px;
  margin-left: 15px;
  margin-right: 5px;
  color: #2e8bd6;
}
.diary_hd-time {
  color: #7788b3;
}
.diary_bd {
  margin: 15px 0;
  font-size: 14px;
}
.diary_bd-photo {
  margin-top: 15px;
  height: 250px;
}
.diary_ft {
  display: flex;
  justify-content: flex-end;
}

/*侧边栏*/
.SideBar {
  margin-left: 45px;
  flex-grow: 1;
  height: 100px;
  background-color: #000;
}
/*页码*/
.page-number {
  width: 960px;
  margin: 30px auto 65px auto;
}
.page-number_bd {
  width: 72%;
  display: flex;
  justify-content: center;
}
.page-number-item {
  width: 26px;
  height: 26px;
  line-height: 26px;
  text-align: center;
  font-size: 14px;
  color: #000;
  background-color: #e7e7e7;
  margin: 0 3px;
}
.page-number-item_active{
  color: #fff;
  background-color: #30b8ff;
}
.page-footer {
  position: fixed;
  bottom: 0;
  width: 100%;
}
.copy-box {
  height: 50px;
  width: 100%;
  border-top: 1px solid #d5d5d5;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f7f7f7;
}
</style>
