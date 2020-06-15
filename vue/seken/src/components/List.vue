<template>
  <div class="">
      <span>{{ name }}</span>
      <span>{{ url }}</span>
  </div>
</template>

<script>
export default {
  name: 'List',
  props: ['input'],
  data () {
    return {
      name: this.input.name,
      url: this.input.url
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
