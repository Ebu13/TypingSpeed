<template>
  <div>
    <HeaderC />
    <InputText/>
    <TextArea :rows="rows"></TextArea>
  </div>
</template>
<script>
import HeaderC from "./components/HeaderC.vue";
import TextArea from "./components/TextArea.vue";
import InputText from "./components/InputText.vue";

export default {
  components: {
    HeaderC,
    TextArea,
    InputText,
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