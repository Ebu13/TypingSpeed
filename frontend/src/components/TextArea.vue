<template>
    <div>
        <div>
            <ul>
                <li v-for="row in rows" :key="row.id">
                    {{ row.row_data }}
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
/* Gerekli stillendirme kodlarını buraya ekleyebilirsiniz */
</style>
  