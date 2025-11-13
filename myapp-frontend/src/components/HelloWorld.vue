<script setup lang="ts">
import { ref, onMounted } from "vue";
import DataService from "../services/DataService.js";
// 在<script setup>中，不需要定义setup()函数// 直接编写逻辑即可，变量会自动暴露给模板
// 初始化数据
const message = ref("");
const items = ref([]);
// 定义一个异步函数来获取数据
const fetchData = async () => {
  try {
    const response = await DataService.getData(); // 将获取的数据设置为组件的响应式属性
    message.value = response.data.message;
    items.value = response.data.items;
  } catch (error) {
    console.error(error);
  }
};
// 在组件挂载时调用 fetchData 函数
onMounted(fetchData);
</script>
<template>
  <div class="hello">
    <h1>{{ message }}</h1>
    <ul>
      <!-- 遍历 items 数组，显示每个元素的内容 -->
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>
<style scoped>
.read-the-docs {
  color: #888;
}
</style>
