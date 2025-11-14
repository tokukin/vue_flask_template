import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

// 导入 Element Plus 组件
import ElementPlus from "element-plus";
// 导入 Element Plus 样式（关键）
import "element-plus/dist/index.css";

const app = createApp(App);
app.use(ElementPlus); // 全局注册组件
app.mount("#app");
