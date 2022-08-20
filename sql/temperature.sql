CREATE DATABASE db_temperature;
USE db_temperature;

CREATE TABLE tbl_temperature(
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_time DATETIME NOT NULL,
    ocean_name VARCHAR(8) NOT NULL,
    temperature INT NOT NULL,
    unit INT
);

ALTER TABLE tbl_temperature AUTO_INCREMENT = 1;