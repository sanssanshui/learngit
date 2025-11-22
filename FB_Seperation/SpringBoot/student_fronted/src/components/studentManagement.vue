<script>
import axios from "axios";
import { reactive, ref, onMounted } from "vue";
import "../style.css";
export default {
  setup() {
    const students = ref([]);
    const student = reactive({ id: "", name: "", score: "" });

    const apiBase = "http://localhost:8081/api/students";

    const getAllStudents = async () => {
      const res = await axios.get(apiBase);
      students.value = res.data;
    };

    const searchStudent = async () => {
      if (!student.id) {
        alert("请输入学号");
        return;
      }
      try {
        const res = await axios.get(`${apiBase}/${student.id}`);
        students.value = [res.data];
      } catch (err) {
        alert("未找到该学生");
      }
    };

    const addStudent = async () => {
      if (!student.name || !student.score) {
        alert("请输入姓名和成绩");
        return;
      }
      await axios.post(apiBase, { name: student.name, score: student.score });
      alert("录入成功");
      getAllStudents();
    };

    const updateStudent = async () => {
      if (!student.id || !student.score) {
        alert("请输入学号和新成绩");
        return;
      }
      await axios.put(`${apiBase}/${student.id}`, {
        name: student.name,
        score: student.score,
      });
      alert("修改成功");
      getAllStudents();
    };

    const deleteStudent = async (id) => {
      if (!confirm("确定删除该学生？")) return;
      await axios.delete(`${apiBase}/${id}`);
      alert("删除成功");
      getAllStudents();
    };

    onMounted(() => {
      getAllStudents();
    });

    return {
      students,
      student,
      getAllStudents,
      searchStudent,
      addStudent,
      updateStudent,
      deleteStudent,
    };
  },
};
</script>
<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <h1 class="text-3xl font-bold text-center text-indigo-700 mb-6">
      学生成绩管理系统
    </h1>

    <!-- 操作表单 -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      <input
        v-model="student.id"
        type="number"
        placeholder="学号"
        class="inputStyle"
      />
      <input
        v-model="student.name"
        type="text"
        placeholder="姓名"
        class="inputStyle"
      />
      <input
        v-model="student.score"
        type="number"
        placeholder="成绩"
        class="inputStyle"
      />
      <div class="flex space-x-2">
        <button @click="addStudent" class="btn-indigo">录入成绩</button>
        <button @click="updateStudent" class="btn-green">修改成绩</button>
      </div>
    </div>

    <!-- 查询按钮 -->
    <div class="flex space-x-4 mb-6">
      <button @click="searchStudent" class="btn-yellow">查询单个学生</button>
      <button @click="getAllStudents" class="btn-blue">查询全班成绩</button>
    </div>

    <!-- 表格显示 -->
    <table class="min-w-full border">
      <thead>
        <tr class="bg-indigo-500 text-white">
          <th class="py-2 border">学号</th>
          <th class="py-2 border">姓名</th>
          <th class="py-2 border">成绩</th>
          <th class="py-2 border">操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="s in students" :key="s.id">
          <td class="py-2 border text-center">{{ s.id }}</td>
          <td class="py-2 border text-center">{{ s.name }}</td>
          <td class="py-2 border text-center">{{ s.score }}</td>
          <td class="py-2 border text-center">
            <button
              @click="deleteStudent(s.id)"
              class="text-red-500 hover:underline"
            >
              删除
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<style scoped></style>
