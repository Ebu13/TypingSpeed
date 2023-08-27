<template>
  <div>
    <ul>
      <li v-for="row in rows.slice( count , count+2 )" :key="row.id">
        <div class="box">
          {{ row.row_data }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    rows: {
      type: Array,
      required: true,
    },
    count:{
      type :Int16Array,
      required:true,
    }
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.box {
  padding: 10px;
  margin: 20px;
  text-align: center;
  list-style-type: none; /* Nokta işaretlerini kaldırmak için bu satırı ekledik */
}
ul{
  list-style-type: none;
}
</style>
