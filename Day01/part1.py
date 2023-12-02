with open("prod.data", "r") as working_data:
    # Initialize a variable to hold our running total
    line_sum = 0
    for line in working_data:
        first_digit = ""
        last_digit = ""
        for character in line:
            if character.isdigit():
                # .isdigit() method under the string class
                # checks if all elements in the string are digits
                if not first_digit:
                    first_digit = character
                last_digit = character
        if first_digit and last_digit:
            # smash the digits together 1 2 becomes 12
            line_total = int(first_digit + last_digit)
            line_sum += line_total
print(line_sum)
