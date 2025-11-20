package com.example.controller;

import java.util.Map;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.Entity.Student;
import com.example.services.studentService;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173")
public class LoginController {
    @Autowired
    private studentService service;
    
    @PostMapping("/login")
    public ResponseEntity<Map<String, Object>> login(@RequestBody Map<String, String> loginRequest) {
        String idString = loginRequest.get("id");
        String password = loginRequest.get("password");

        if (idString == null || password == null) {
            return ResponseEntity.badRequest().body(Map.of("success", false, "message", "缺少学号或密码"));
        }
        
            try {
            Long id = Long.parseLong(idString);
            Optional<Student> studentOpt = service.getStudentById(id);

            if (studentOpt.isPresent() && password.equals(studentOpt.get().getPassword())) {
                return ResponseEntity.ok(Map.of(
                    "success", true,
                    "student", studentOpt.get()
                ));
            } else {
                return ResponseEntity.ok(Map.of("success", false, "message", "学号或密码错误"));
            }
        } catch (NumberFormatException e) {
            return ResponseEntity.badRequest().body(Map.of("success", false, "message", "学号格式错误"));
        }
    }
   }


