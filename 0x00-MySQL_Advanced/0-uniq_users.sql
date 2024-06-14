-- Script to create a users table
CREATE DATABASE IF NOT EXISTS holberton;
USE `holberton`;
CREATE TABLE IF NOT EXISTS holberton.users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
