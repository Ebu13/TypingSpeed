<template>
  <div>
    <HeaderC/>
    <!--<TextArea :rows="rows"></TextArea>-->
  </div>
</template>
<script>
import HeaderC from "./components/HeaderC.vue";
import TextArea from "./components/TextArea.vue";

export default {
  components: {
    HeaderC,
    TextArea,
  },
  data() {
    return {
      rows: []
    };
  },
  mounted() {
    fetch('http://127.0.0.1:8000/rows')
      .then(response => response.json())
      .then(data => {
        this.rows = data.rows;
      });
  }
};
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
