import Vue from 'vue'
import App from './app'
import store from '../../store'
const app = new Vue({
  el: '#app',
  store,
  render: h => h(App)
})