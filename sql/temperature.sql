CREATE DATABASE db_temperature;
USE db_temperature;

CREATE TABLE tbl_temperature(
    id INT PRIMARY KEY AUTO_INCREMENT,
    temperature INT NOT NULL,
    unit INT,
    ocean_name VARCHAR(8) NOT NULL,
    date_time DATETIME NOT NULL
);

ALTER TABLE tbl_temperature AUTO_INCREMENT = 1;