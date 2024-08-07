CREATE DATABASE IF NOT EXISTS task_manager;

USE task_manager;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY,
    salary DECIMAL(10, 2) NOT NULL
);
