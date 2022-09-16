DROP DATABASE IF EXISTS db_temperature;
CREATE DATABASE db_temperature;
USE db_temperature;

CREATE TABLE tbl_temperature(
    id INT PRIMARY KEY AUTO_INCREMENT,
    temperature DECIMAL(18, 2),
    unit CHAR(2),
    date_time VARCHAR(255)
);

ALTER TABLE tbl_temperature AUTO_INCREMENT = 1;