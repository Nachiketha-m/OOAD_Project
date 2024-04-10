package com.example;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class AppController {

    @Autowired
    private UserRepository userRepo;

    @GetMapping("")
    public String viewHomePage() {
        return "index";
    }

    @GetMapping("/login1")
    public String showLoginForm() {
        return "login"; // assuming "login.html" is the Thymeleaf template for login
    }

    @GetMapping("/register")
    public String showRegistrationForm(Model model) {
        model.addAttribute("user", new User());
        return "signup_form";
    }

    @GetMapping("/users")
    public String listUsers(Model model) {
        List<User> listUsers = userRepo.findAll();
        model.addAttribute("listUsers", listUsers);
        return "users";
    }

    @PostMapping("/process_register")
    public String processRegistration(User user) {
        // Save user to the database
        userRepo.save(user);
        return "registration_success";
    }

    @PostMapping("/login")
    public String login(User user) {
        User existingUser = userRepo.findByUsername(user.getusername());
        if (existingUser != null && existingUser.getpassword().equals(user.getpassword())) {
            return "Login successful";
        } else {
            return "Invalid username or password";
        }
    }
}
