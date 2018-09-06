import Vue from 'vue'
import vuex from 'vuex'
Vue.use(vuex);
import login from './login.js'
import data from './index_data.js'
import myDiaryData from './myDiary.js'
import ip from "./ip.js"
export default new vuex.Store({
    modules:{
        login:login,
        data:data,
        ip:ip,
        myDiaryData:myDiaryData
    }
})