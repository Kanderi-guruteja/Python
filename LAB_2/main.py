import datetime

print("BMI Calculator")

unit = input("Choose an option to enter the weight and height: English units or Metric units? ")
unit = unit.lower()

if unit == "english":
    try:
        weight = float(input("Please enter your weight in pounds: "))
        height = float(input("Please enter your height in inches: "))

        BMI = (weight * 703) / (height ** 2)

        print("BMI is %.2f" % BMI)

        if BMI < 18.5:
            print("Person is underweight")
        elif 18.5 <= BMI <= 24.9:
            print("Person is normal")
        elif 25.0 <= BMI <= 29.9:
            print("Person is overweight")
        else:
            print("Person is obese")
    except ValueError:
        print("Invalid input for weight. Please enter a valid number.")

elif unit == "metric":
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))

        BMI = weight / (height ** 2)

        print("BMI is %.2f" % BMI)

        if BMI < 18.5:
            print("Person is underweight")
        elif 18.5 <= BMI <= 24.9:
            print("Person is normal")
        elif 25.0 <= BMI <= 29.9:
            print("Person is overweight")
        else:
            print("Person is obese")
    except ValueError:
        print("Invalid input for weight. Please enter a valid number.")

else:
    print("Invalid input. Please choose either 'English' or 'Metric'.")

now = datetime.datetime.now()
# Author: Guruteja Kanderi
print("Author: Guruteja Kanderi")
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Motivational Quote
quote = "Remember, a healthy outside starts from the inside. - Robert Urich"
print(quote)
