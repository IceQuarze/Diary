import fetch from "../fetch.js"
export default{
    state:{
        show:false,
        isLogin:fetch.storage.get('isLogin'),
        userName:fetch.storage.get('userName'),
    },
    mutations:{
        turnOnLoginModal(state){
            state.show=true;
        },
        turnOffLoginModal(state){
            state.show=false;
        },
        update(state){
            state.isLogin=fetch.storage.get("isLogin")
            state.userName=fetch.storage.get('userName')
        }
    }
}