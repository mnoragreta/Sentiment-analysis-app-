CREATE DATABASE IF NOT EXISTS Model_Logger;

USE Model_Logger;

-- Create the Log table
CREATE TABLE IF NOT EXISTS Log (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Current_Date_Time DATETIME,
    Input_Params VARCHAR(255),
    Output VARCHAR(255),
    Response_Time FLOAT
);

-- Create the mlops table
CREATE TABLE IF NOT EXISTS mlops (
    ID INT PRIMARY KEY AUTO_INCREMENT
);

-- Alter user root password for compatibility
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;
