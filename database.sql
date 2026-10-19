-- ============================================================
-- SQL SCHEMA FOR INFORMATICS PRACTICES CAPSTONE PROJECT
-- SYSTEM ARCHITECTURE FOR REGIONAL HOSPITAL MANAGEMENT
-- AUTHOR: SHUBHANGINI SHREYA
-- ============================================================

CREATE DATABASE IF NOT EXISTS project;
USE project;

-- ------------------------------------------------------------
-- 1. CLASSIFIED ACCESS CREDENTIAL MODULE (USERS)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password) VALUES
('Aditi', 'Aditi123'),
('Anandi', 'Anandi123'),
('Ananya', 'Ananya123'),
('Jiya', 'Jiya123'),
('Shubhangini', 'Shubhangini123');

-- ------------------------------------------------------------
-- 2. CLINICAL STAFF MATRIX LAYER (DOCTOR_DETAILS)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doctor_details (
    d_name VARCHAR(100) NOT NULL,
    d_age INT NOT NULL,
    d_department VARCHAR(100) NOT NULL,
    d_phone BIGINT PRIMARY KEY
);

INSERT INTO doctor_details (d_name, d_age, d_department, d_phone) VALUES
('Arushi', 35, 'Cardiology', 9000000001),
('Shreyashi', 40, 'Neurology', 9000000002),
('Madhuri', 38, 'Orthopedics', 9000000003),
('Tharn', 45, 'Dermatology', 9000000004),
('Arushi Lakra', 17, 'Orthopaedic', 9608386149),
('Arushi', 18, 'Orthopaedic', 9608386149),
('Ragini', 86, 'Psychiatric', 4653178952),
('Gem', 86, 'Orthopaedic', 4521378521);

-- ------------------------------------------------------------
-- 3. MEDICAL ENTRY MATRIX LAYER (PATIENT_DETAILS)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS patient_details (
    p_name VARCHAR(100) NOT NULL,
    p_age INT NOT NULL,
    p_problem VARCHAR(255) NOT NULL,
    p_phone BIGINT PRIMARY KEY
);

INSERT INTO patient_details (p_name, p_age, p_problem, p_phone) VALUES
('Shubhangini', 17, 'Fever', 9876543210),
('Anandi', 18, 'Headache', 9876543211),
('Aditi', 19, 'Cold', 9876543212),
('Jiya', 18, 'Stomach Pain', 9876543213),
('Ananya', 20, 'Cough', 9876543214),
('Manya', 17, 'Migrane', 9035625315),
('Manya', 78, 'Chronic Fatigue Syndrome', 4561236985);

-- ------------------------------------------------------------
-- 4. AUXILIARY SERVICE ARCHITECTURE LAYER (WORKER_DETAILS)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS worker_details (
    w_name VARCHAR(100) NOT NULL,
    w_age INT NOT NULL,
    w_work VARCHAR(100) NOT NULL,
    w_phone BIGINT PRIMARY KEY
);

INSERT INTO worker_details (w_name, w_age, w_work, w_phone) VALUES
('Joong', 25, 'Lab Technician', 8100000001),
('Dunk', 24, 'Ward Clerk', 8100000002),
('Pond', 26, 'Radiology Assistant', 8100000003),
('Phwin', 21, 'Data Entery Operator', 8100000004),
('Fourth', 20, 'Pharmacy Intern', 8100000005),
('William', 22, 'Medical Record Clerk', 8100000006),
('Santa', 28, 'Sanitation Coordinator', 8100000007),
('Perth', 23, 'Front Desk Executive', 8100000008),
('Li', 45, 'Security Supervisor', 3698512589);
