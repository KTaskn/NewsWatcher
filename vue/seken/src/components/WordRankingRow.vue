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
export default {
  name: 'WordRankingRow',
  props: ['date', 'words'],
  mounted () {
  },
  data () {
    return {
      format_date: this.date.format('YYYY年MM月DD日')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
