import axios from "axios";

// 创建一个 axios 实例，用于发送请求
const apiClient = axios.create({
  // 设置后端 API 的基础 URL
  baseURL: "http://localhost:5000/api/user",
  // 设置请求头
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// 定义一个用于获取数据的函数
export default {
  getData(user_id: number) {
    // 向 '/data' 路由发送 GET 请求
    return apiClient.get(`/info?user_id=${user_id}`);
  },
};
