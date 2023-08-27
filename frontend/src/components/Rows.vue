<template>
  <div>
    <ul>
      <li v-for="row in rows" :key="row.id">
        {{ row.id }} : {{ row.row_data }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
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
