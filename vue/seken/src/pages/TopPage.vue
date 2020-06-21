<template>
  <div class="toppage">
    <WordRankingRow
    class="datalist"
    v-for="row in word_ranking_rows"
    v-bind:key="row.id"
    v-bind:date="row.date"
    v-bind:words="row.words"></WordRankingRow>
  </div>
</template>

<script>
import moment from 'moment'

import Global from '@/global/index'
import WordRankingRow from '@/components/WordRankingRow'

export default {
  name: 'TopPage',
  data () {
    return {
      word_ranking_rows: [
      ]
    }
  },
  mounted () {
    var today = moment('20200621', 'YYYYMMDD')
    this.get_wordranking(today, {
      'year': today.year(),
      // なぜか0スタート
      'month': today.month() + 1,
      'date': today.date(),
      'limit': 5
    })
  },
  components: {
    WordRankingRow
  },
  methods: {
    get_wordranking (date, data = {}) {
      var url = '/wordranking/'
      return Global.get_wrapper(
        url,
        data
      ).then((res) => {
        var tmp = {
          'date': date,
          'words': []
        }
        res.data.results.forEach((ent) => {
          tmp.words.push(ent)
        })
        this.word_ranking_rows.push(tmp)
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
</style>
