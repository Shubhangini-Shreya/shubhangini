# Hospital Management System (HMS)
### Relational Database E-Ecosystem & Data Management System

A custom-engineered desktop application designed to streamline administrative healthcare operations, patient tracking, and internal hospital workflows. Developed as a final High School Informatics Practices (IP) Capstone Project to demonstrate proficiency in relational database architecture, structural logic, and object-oriented programming.

## 🚀 Core Features
* **Relational Database Design:** Built a structured data schema ensuring data integrity across multi-tiered patient registries, doctor allocations, and billing records.
* **Automated Computation:** Integrates programmatic modules for calculated metrics, including patient billing logs and staff shift mapping.
* **Data Persistence:** Implemented persistent storage mechanisms via structured SQL queries, eliminating data loss across application lifecycles.
* **Error Handling & Validation:** Structured with runtime exception blocks to catch user input errors, verifying data sanity before committing changes to the backend database.

## 🛠️ Technical Architecture & Stack
* **Primary Language:** Python 3.x
* **Database Engine:** MySQL Server
* **Database Driver:** `mysql-connector-python`
* **Interface Design:** Structured Terminal Interface / Command-Line Engine

## 💻 System Configuration & Local Deployment
To deploy and explore this management ecosystem locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd shubhangini
   ```

2. **Configure the Database Pipeline:**
   * Open your local MySQL command line interface.
   * Import the underlying database configuration file (`database.sql`) included in the project directory to build the relational schema.

3. **Install Core Dependencies:**
   ```bash
   pip install mysql-connector-python
   ```

4. **Execute the Application Engine:**
   ```bash
   python "IP project.py"
   ```
