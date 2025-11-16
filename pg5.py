# Program to calculate Simple Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("The Simple Interest is:", simple_interest)
