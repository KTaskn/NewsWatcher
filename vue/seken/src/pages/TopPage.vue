<template>
  <div class="toppage">
    <List
      v-for="ent in mylist"
      v-bind:key="ent.id"
      v-bind:input="ent"></List>
  </div>
</template>

<script>
import Global from '@/global/index'
import List from '@/components/List'

export default {
  name: 'TopPage',
  data () {
    return {
      mylist: [
      ]
    }
  },
  mounted () {
    this.get_newspaper()
  },
  components: {
    List
  },
  methods: {
    get_newspaper (data = {}) {
      var url = '/newspapers/'
      return Global.get_wrapper(
        url,
        data
      ).then((res) => {
        this.mylist = res.data.results
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
