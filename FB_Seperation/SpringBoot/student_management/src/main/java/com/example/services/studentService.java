package com.example.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

import com.example.Entity.Student;
import com.example.repository.studentRepository;



@Service

public class studentService {

    @Autowired
    private studentRepository studentConnector;
   
    public List<Student> getAllStudents() {
        return studentConnector.findAll();
    }

    public Optional<Student> getStudentById(Long id) {
        return studentConnector.findById(id);
    }


    public Student saveStudent(Student student) {
        return studentConnector.save(student);
    }

    public void deleteStudent(Long id) {
        studentConnector.deleteById(id);
    }

     public Student updateStudent(Long id, Student updated) {
        return studentConnector.findById(id).map(s -> {
            s.setName(updated.getName());
            s.setPassword(updated.getPassword());
            s.setScore(updated.getScore());
            return studentConnector.save(s);
        }).orElseGet(() -> {           
            updated.setId(id);
            return studentConnector.save(updated);
        });
    }

}

