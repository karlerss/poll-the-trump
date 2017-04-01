import Vue from 'vue'
import App from './App.vue'
import Tweet from 'vue-tweet-embed'


Vue.use(require('vue-resource'));
Vue.component('Tweet', Tweet);
new Vue({
    el: '#app',
    render: h => h(App)
})

