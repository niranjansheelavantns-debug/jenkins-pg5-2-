# Palindrome Checker using sys.argv and if-else

import sys

# Check if the user has provided exactly 1 argument (the string to check)
if len(sys.argv) != 2:
    print("Usage: python palindrome.py <string>")
    sys.exit(1)
else:
    # Extract the string argument
    text = sys.argv[1]

    # Convert to lowercase for case-insensitive comparison
    text_lower = text.lower()

    # Reverse the string
    reversed_text = text_lower[::-1]

    # Check if palindrome using if-else
    if text_lower == reversed_text:
        print(f"'{text}' is a palindrome.")
    else:
        print(f"'{text}' is not a palindrome.")