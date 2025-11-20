<script>
import axios from "axios";

export default {
  name: "MainPage",
  data() {
    return {
      id: "",
      password: "",
    };
  },
  methods: {
    async login() {
      if (!this.id || !this.password) {
        alert("请填写学号和密码");
        return;
      }

      try {
        const res = await axios.post("http://localhost:8081/api/login", {
          id: this.id,
          password: this.password,
        });

        if (res.data.success) {
          this.$router.push("/score");
        } else {
          alert("学号或密码错误");
        }
      } catch (err) {
        console.error(err);
        alert("登录失败，请检查后端服务");
      }
    },
  },
};
</script>
<template>
  <div
    class="min-h-screen flex flex-col justify-center bg-linear-to-br from-indigo-800 to-gray-900 px-6 py-12"
  >
    <div class="mx-auto w-full max-w-sm">
      <img src="../assets/five.jpg" alt="Logo" class="mx-auto h-14" />
      <h2 class="mt-6 text-center text-3xl font-bold text-white">学生登录</h2>
    </div>

    <div
      class="mt-8 mx-auto w-full max-w-sm bg-white/10 backdrop-blur-xl p-6 rounded-xl shadow-xl"
    >
      <div class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-indigo-200">学号</label>
          <input
            v-model="id"
            type="text"
            placeholder="请输入学号"
            class="mt-1 w-full rounded-lg px-3 py-2 bg-white/20 text-white placeholder-gray-200 outline-none"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-indigo-200">密码</label>
          <input
            v-model="password"
            type="password"
            placeholder="请输入密码"
            class="mt-1 w-full rounded-lg px-3 py-2 bg-white/20 text-white placeholder-gray-200 outline-none"
          />
        </div>

        <button
          @click="login"
          class="w-full py-2 rounded-lg bg-indigo-500 text-white text-lg font-bold hover:bg-indigo-400"
        >
          登录
        </button>

        <p class="text-center text-sm text-indigo-200">
          还没有账号？
          <span class="underline cursor-pointer hover:text-white"
            >立即注册</span
          >
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
