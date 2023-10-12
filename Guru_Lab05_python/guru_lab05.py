import os

def calculate_gross_pay(rate, hours):
    if hours > 40:
        regular_pay = rate * 40
        overtime_hours = hours - 40
        overtime_pay = rate * 1.5 * overtime_hours
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = rate * hours
    return gross_pay


def print_all():
    file_name = "employees.txt"  # Assuming the file is named employees.txt
    try:
        with open(file_name, "r") as emp_file:
            for line in emp_file:
                line = line.split(" ")
                first_name = line[0]
                last_name = line[1]
                rate = float(line[2])
                hours = float(line[3])
                name = first_name + " " + last_name
                gross_pay = calculate_gross_pay(rate, hours)
                print(f"{name}: ${gross_pay:.2f}")
    except FileNotFoundError:
        print("Error: Payroll file not found.")


def print_employee():
    file_name = "employees.txt"  # Assuming the file is named employees.txt
    name = input("Enter the name of the employee: ")
    try:
        with open(file_name, "r") as emp_file:
            for line in emp_file:
                line = line.split(" ")
                first_name = line[0]
                last_name = line[1]
                rate = float(line[2])
                hours = float(line[3])
                if name == first_name + " " + last_name:
                    gross_pay = calculate_gross_pay(rate, hours)
                    print(f"{name}: ${gross_pay:.2f}")
                    break
            else:
                print("Employee not found.")
    except FileNotFoundError:
        print("Error: Payroll file not found.")


def add_employee():
    file_name = "employees.txt"  # Assuming the file is named employees.txt
    first_name = input("Enter the first name of the employee: ")
    last_name = input("Enter the last name of the employee: ")
    rate = float(input("Enter the rate of pay: "))
    hours = float(input("Enter the number of hours worked: "))

    try:
        with open(file_name, "a") as emp_file:
            emp_file.write(f"{first_name} {last_name} {rate} {hours}\n")
        print("Employee record added successfully.\n")
    except FileNotFoundError:
        print("Error: Payroll file not found.\n")


def delete_employee():
    file_name = "employees.txt"  # Assuming the file is named employees.txt
    first_name = input("Enter the first name of the employee to delete: ")
    last_name = input("Enter the last name of the employee to delete: ")

    try:
        with open(file_name, "r") as emp_file:
            lines = emp_file.readlines()

        found = False
        with open(file_name, "w") as emp_file:
            for line in lines:
                if line.startswith(f"{first_name} {last_name}"):
                    found = True
                else:
                    emp_file.write(line)

        if found:
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("Error: Payroll file not found.")


def modify_employee():
    file_name = "employees.txt"  # Assuming the file is named employees.txt
    first_name = input("Enter the first name of the employee to modify: ")
    last_name = input("Enter the last name of the employee to modify: ")

    try:
        with open(file_name, "r") as emp_file:
            lines = emp_file.readlines()

        found = False
        with open(file_name, "w") as emp_file:
            for line in lines:
                if line.startswith(f"{first_name} {last_name}"):
                    rate = float(input("Enter the new rate of pay: "))
                    hours = float(input("Enter the new number of hours worked: "))
                    line = f"{first_name} {last_name} {rate} {hours}\n"
                    found = True
                emp_file.write(line)

        if found:
            print("Employee record modified successfully.\n")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("Error: Payroll file not found.")


def exit_app():
    print("Thank you for using the Payroll Program!")
    exit()
