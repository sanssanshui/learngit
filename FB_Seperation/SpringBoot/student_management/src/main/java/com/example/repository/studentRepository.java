package com.example.repository;

import com.example.Entity.Student;



import org.springframework.data.jpa.repository.JpaRepository;

public interface studentRepository extends JpaRepository<Student, Long> {

} 
