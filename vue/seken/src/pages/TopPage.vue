<template>
  <div class="toppage">
    <WordRankingRow
    class="datalist"
    v-for="row in word_ranking_rows"
    :key="row.id"
    :date="row.date"></WordRankingRow>
    </div>
</template>

<script>
import moment from 'moment'

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
    for (var num = 0; num < 30; num++) {
      var date = moment().add('days', -num)
      this.word_ranking_rows.push({'date': date})
    }
  },
  components: {
    WordRankingRow
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
</style>
