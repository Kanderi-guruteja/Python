from guru_lab05 import *


def menu():
    pstr = "Choose from the following payroll choices:\n"
    pstr += "(1) Display a gross payroll report for all employees\n"
    pstr += "(2) Display a gross payroll report for a single employee by name\n"
    pstr += "(3) Add an employee record\n"
    pstr += "(4) Delete an employee record\n"
    pstr += "(5) Modify an employee record\n"
    pstr += "(6) Exit program"
    print(pstr)


def gurumain():
    while True:
        menu()
        choice = int(input("Enter Menu Choice Now! "))

        if choice == 1:
            print_all()
        elif choice == 2:
            print_employee()
        elif choice == 3:
            add_employee()
        elif choice == 4:
            delete_employee()
        elif choice == 5:
            modify_employee()
        elif choice == 6:
            exit_app()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    gurumain()
