import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../components/MainPage.vue";
import studentManagement from "../components/studentManagement.vue";

const routes = [
  { path: "/", name: "login", component: MainPage },
  { path: "/score", name: "studentManagement", component: studentManagement },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
