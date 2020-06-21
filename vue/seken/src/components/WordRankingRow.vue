<template>
  <div class="">
    <span>{{ format_date }}</span>
    <span
      v-for="a_word in words"
      v-bind:key="a_word.id"
      v-bind:input="a_word">{{ a_word.word }} /</span>
  </div>
</template>

<script>
import Global from '@/global/index'
export default {
  name: 'WordRankingRow',
  props: ['date'],
  mounted () {
    this.get_wordranking(
      this.date,
      {
        'year': this.date.year(),
        // なぜか0スタート
        'month': this.date.month() + 1,
        'date': this.date.date(),
        'limit': 5
      })
  },
  data () {
    return {
      format_date: this.date.format('YYYY年MM月DD日'),
      words: []
    }
  },
  methods: {
    get_wordranking: function (date, data = {}, num = 1) {
      var url = '/wordranking/'
      return Global.get_wrapper(
        url,
        data
      ).then((res) => {
        this.words.push(data.date)
        res.data.results.forEach((ent) => {
          this.words.push(ent)
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
