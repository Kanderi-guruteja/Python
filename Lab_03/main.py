#Author: Guruteja_Kanderi
#LAB_03_Loops and repetition - Bank Account Activity
#A20526883
#6/19/23 13:13 PM
print("GURUTEJA_KANDERI\nA20326883\nLAB_03:BANK ACCOUNT ACTIVITY")

# Define the correct PIN
correct_pin = "1234"
max_attempts = 3 # Allows the user to attempt to enter the PIN 3 times Max if it is wrong.
print("WELCOME TO THE BANK OF IIT") # Display the welcome message

# Prompt user to enter the PIN
for attempt in range(max_attempts, 0, -1):
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN accepted. Access has been granted.") # Allows user to enter the Initial amount and interest rate.
        break
    else:
        print(f"Invalid PIN, Please enter the correct PIN. {attempt-1} attempts remaining.")
else:
    print("Max attempts have been reached. Exiting program. Thank you!")

# Prompt the user for the initial bank balance and annual interest rate
bank_balance = float(input("Enter an initial bank balance: "))

interest_rate_input = input("Enter the annual interest rate: ")
if "%" in interest_rate_input:
    # Convert the percentage to a decimal so that it recognizes when a person enters "%" instead of decimals.
    interest_rate = float(interest_rate_input.strip("%")) / 100
else:
    # Assume the input is already a decimal
    interest_rate = float(interest_rate_input)

# Calculate and display the new balance for each month over a 12-month period
print("\nMonth #\tInterest Amt\tBalance")
for month in range(1, 13):
    interest = bank_balance * (interest_rate / 12)
    bank_balance += interest
    print(f"{month}\t\t{interest:.2f}\t\t\t{bank_balance:.2f}")

# Calculate and print the total amount after 12 months
total_amount = bank_balance
print(f"\nTotal amount after 12 months: {total_amount:.2f}") #printing the final balance
