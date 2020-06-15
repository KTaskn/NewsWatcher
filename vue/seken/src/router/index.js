import Vue from 'vue'
import Router from 'vue-router'
import TopPage from '@/pages/TopPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TopPage',
      component: TopPage
    }
  ]
})
