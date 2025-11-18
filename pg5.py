import sys

# Check if the correct number of arguments is passed
if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
else:
         # Convert inputs to float
        principal = float(sys.argv[1])
        rate = float(sys.argv[2])
        time = float(sys.argv[3])

        # Validate that all inputs are positive
        if principal <= 0:
            print("Error: Principal amount must be greater than 0.")
        elif rate <= 0:
            print("Error: Rate of interest must be greater than 0.")
        elif time <= 0:
            print("Error: Time must be greater than 0.")
        else:
            # Calculate simple interest
            simple_interest = (principal * rate * time) / 100
            print("Simple Interest =", simple_interest)


