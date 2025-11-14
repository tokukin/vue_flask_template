<script setup lang="ts">
import { ref, onMounted } from "vue";
import { ElSelect, ElOption } from "element-plus";
import DataService from "../services/DataService.js";
// 在<script setup>中，不需要定义setup()函数// 直接编写逻辑即可，变量会自动暴露给模板
// 初始化数据

// 定义数据类型（TypeScript 类型约束）
interface UserOption {
  id: number;
  name: string;
}

interface UserData {
  message: string;
  // 其他用户信息字段（根据实际接口返回补充）
  [key: string]: any; // 允许其他未知字段
}

// 初始化数据（指定类型，避免 any）
const message = ref<string>("");
const item = ref<UserData>({} as UserData); // 初始化为空对象并断言类型

// 选项数据（明确类型）
const options: UserOption[] = [
  { id: 1, name: "用户1" },
  { id: 2, name: "用户2" },
];

// 选中的值（类型为 number | ""，因为选项id是number，初始为空字符串）
const selectedId = ref<number | "">("");
const title = "Flask+Vue+Vite hello";
// 定义异步函数（参数指定类型）
const fetchData = async (id: number) => {
  try {
    const response = await DataService.getData(id);
    // 假设接口返回格式为 { data: { message: string, ... } }

    item.value = response.data.data;
    message.value = response.data.data.message;
  } catch (error) {
    console.error("获取数据失败：", error);
    message.value = "获取数据失败，请重试"; // 错误提示
  }
};

// 处理选择变化（兼容初始空值）
const handleSelectChange = () => {
  if (selectedId.value) {
    fetchData(selectedId.value); // 只有选中有效id时才请求
  } else {
    // 清空选择时重置数据
    item.value = {} as UserData;
    message.value = "未选择用户";
  }
};

// 在组件挂载时调用 fetchData 函数
//onMounted(fetchData);
</script>

<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <div>
      <label>选择用户：</label>
      <!-- 使用 Element Plus 的 ElSelect 更美观，且兼容 TS -->
      <ElSelect
        v-model="selectedId"
        placeholder="请选择用户"
        @change="handleSelectChange"
      >
        <ElOption
          v-for="opt in options"
          :key="opt.id"
          :label="opt.name"
          :value="opt.id"
        />
      </ElSelect>
    </div>

    <p v-if="Object.keys(item).length">获取到的用户信息：{{ item }}</p>
    <p v-else-if="selectedId">暂无用户信息</p>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
/* 给选择框添加一点样式 */
.el-select {
  margin-left: 8px;
  width: 200px;
}
</style>
