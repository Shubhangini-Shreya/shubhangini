import mysql.connector as sql
from sys import exit

# ---------- DATABASE CONNECTION ----------
conn = sql.connect(
    host='localhost',
    user='root',
    passwd='shu123shr',
    database='project'
)

if conn.is_connected():
    print("Successfully connected to MySQL database")

c1 = conn.cursor()

print("---------------------------------------------")
print("         HOSPITAL MANAGEMENT SYSTEM          ")
print("---------------------------------------------")
print('"GOD WISHES YOU"')

print("1. LOGIN")
print("2. EXIT")

main_choice = int(input("ENTER YOUR CHOICE: "))

# ------------------ LOGIN ------------------
if main_choice == 1:

    username = input("Enter username: ")
    password = input("Enter password: ")

    c1.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = c1.fetchall()

    if result:
        print("Login Successful!")
        print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM\n")

        while True:
            print("---------------------------------------------")
            print("1. Register Patient Details")
            print("2. Register Doctor Details")
            print("3. Register Worker Details")
            print("4. Show All Patient Details")
            print("5. Show All Doctor Details")
            print("6. Show All Worker Details")
            print("7. Search Patient by Name")
            print("8. Search Doctor by Name")
            print("9. Search Worker by Name")
            print("10. Exit")
            print("---------------------------------------------")

            ch = int(input("ENTER YOUR CHOICE: "))

            # ----- PATIENT REGISTRATION -----
            if ch == 1:
                p_name = input("Enter Patient Name: ")
                p_age = int(input("Enter Age: "))
                p_problem = input("Enter Problem/Disease: ")
                p_phone = int(input("Enter Phone Number: "))

                sql_insert = "INSERT INTO patient_details VALUES (%s, %s, %s, %s)"
                data = (p_name, p_age, p_problem, p_phone)
                c1.execute(sql_insert, data)
                conn.commit()
                print("Patient Registered Successfully!\n")

            # ----- DOCTOR REGISTRATION -----
            elif ch == 2:
                d_name = input("Enter Doctor Name: ")
                d_age = int(input("Enter Age: "))
                d_department = input("Enter Department: ")
                d_phone = int(input("Enter Phone Number: "))

                sql_insert = "INSERT INTO doctor_details VALUES (%s, %s, %s, %s)"
                data = (d_name, d_age, d_department, d_phone)
                c1.execute(sql_insert, data)
                conn.commit()
                print("Doctor Registered Successfully!\n")

            # ----- WORKER REGISTRATION -----
            elif ch == 3:
                w_name = input("Enter Worker Name: ")
                w_age = int(input("Enter Age: "))
                w_work = input("Enter Type of Work: ")
                w_phone = int(input("Enter Phone Number: "))

                sql_insert = "INSERT INTO worker_details VALUES (%s, %s, %s, %s)"
                data = (w_name, w_age, w_work, w_phone)
                c1.execute(sql_insert, data)
                conn.commit()
                print("Worker Registered Successfully!\n")

            # ----- SHOW ALL PATIENTS -----
            elif ch == 4:
                c1.execute("SELECT * FROM patient_details")
                records = c1.fetchall()
                print("\n--- Patient Details ---")
                for row in records:
                    print(row)
                print()

            # ----- SHOW ALL DOCTORS -----
            elif ch == 5:
                c1.execute("SELECT * FROM doctor_details")
                records = c1.fetchall()
                print("\n--- Doctor Details ---")
                for row in records:
                    print(row)
                print()

            # ----- SHOW ALL WORKERS -----
            elif ch == 6:
                c1.execute("SELECT * FROM worker_details")
                records = c1.fetchall()
                print("\n--- Worker Details ---")
                for row in records:
                    print(row)
                print()

            # ----- SEARCH PATIENT -----
            elif ch == 7:
                name = input("Enter Patient Name to Search: ")
                query = "SELECT * FROM patient_details WHERE p_name = %s"
                c1.execute(query, (name,))
                result = c1.fetchall()
                print("\nRecord Found:" if result else "\nNo record found.")
                print(result, "\n")

            # ----- SEARCH DOCTOR -----
            elif ch == 8:
                name = input("Enter Doctor Name to Search: ")
                query = "SELECT * FROM doctor_details WHERE d_name = %s"
                c1.execute(query, (name,))
                result = c1.fetchall()
                print("\nRecord Found:" if result else "\nNo record found.")
                print(result, "\n")

            # ----- SEARCH WORKER -----
            elif ch == 9:
                name = input("Enter Worker Name to Search: ")
                query = "SELECT * FROM worker_details WHERE w_name = %s"
                c1.execute(query, (name,))
                result = c1.fetchall()
                print("\nRecord Found:" if result else "\nNo record found.")
                print(result, "\n")

            # ----- EXIT -----
            elif ch == 10:
                print("Exiting system. Thank you!")
                exit()

            else:
                print("Invalid choice. Try again!\n")

    else:
        print("Incorrect username or password.")

# ------------------ EXIT OPTION ------------------
elif main_choice == 2:
    exit()

else:
    print("Invalid Input!")
