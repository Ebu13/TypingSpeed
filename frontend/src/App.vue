<template>
  <div>
    <h1>Typing Game</h1>
    <TextArea :rows="rows" :count="count"></TextArea>
    <InputText v-model="metin" />
    <p>{{ metin }}</p>
    <button @click="increaseCount">{{ count }}</button>
  </div>
</template>

<script>
import TextArea from './components/TextArea.vue';
import InputText from './components/InputText.vue';

export default {
  components: {
    TextArea,
    InputText,
  },
  data() {
    return {
      rows: [],
      count: 0,
      metin:"",
    };
  },
  mounted() {
    fetch('http://127.0.0.1:8000/rows')
      .then(response => response.json())
      .then(data => {
        this.rows = data.rows;
      });
  },
  methods: {
    increaseCount() {
      this.count++;
    },
  },
};
</script>
