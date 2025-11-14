// src/router/index.ts
import { createRouter, createWebHistory } from "vue-router";
// 关键：使用 import type 导入 RouteRecordRaw 类型
import type { RouteRecordRaw } from "vue-router";

// 导入页面组件（按需导入）
import Home from "../views/Home.vue";

// 定义路由规则
const routes: RouteRecordRaw[] = [
  {
    path: "/", // 路由路径
    name: "Home", // 路由名称（可选）
    component: Home, // 对应组件
  },

  {
    // 404 路由（放在最后）
    path: "/:pathMatch(.*)*", // 匹配所有未定义的路由
    name: "NotFound",
    component: () => import("../views/NotFound.vue"), // 懒加载 404 页面
  },
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // HTML5 历史模式（无 #）
  // history: createWebHashHistory(), // 哈希模式（带 #）
  routes, // 注入路由规则
});

export default router;
