package com.example.Entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;
@Entity
@Getter
@Setter
@Table(name = "studentinfo")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

   
    private String name;
    private String password; 
    private int score;
    
    public Student() {
    };
    public Student(String name, int score,String password) {
        this.name = name;    
        this.score = score;
        this.password = password;
    }
    
    @Override
    public String toString() {
        return "Student [name=" + name + ", password=" + password + ", id=" + id + ", score=" + score + "]";
    }
  
}
