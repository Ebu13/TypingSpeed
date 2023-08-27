<template>
    <div>
      <div class="container">
        <ul>
          <li v-for="row in rows" :key="row.id">
            <div class="box">
              {{ row.row_data }}
            </div>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      rows: {
        type: Array,
        required: true,
      },
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
    border: 1px solid black;
    padding: 10px;
    margin: 10px;
    text-align: center;
  }
  </style>
  