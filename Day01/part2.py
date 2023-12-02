import re

# Dictionary mapping number words to digits
number_words = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9
}


def extract_numeric_values_from_mixed_string(line):
    # Regular expression to match number words and digits within mixed strings
    pattern = r'(' + '|'.join(number_words.keys()) + r'|\d)'
    matches = re.findall(pattern, line.lower())

    numeric_values = []
    for match in matches:
        if match.isdigit():
            numeric_values.append(int(match))
        elif match in number_words:
            numeric_values.append(number_words[match])

    return numeric_values


cumulative_sum = 0
with open("prod.data", "r") as working_data:
    lines = working_data.read().splitlines()

    for line in lines:
        numeric_values = extract_numeric_values_from_mixed_string(line)

        if numeric_values:
            first = numeric_values[0]
            last = numeric_values[-1]

            line_total = int(str(first) + str(last))
            cumulative_sum += line_total

print(cumulative_sum)
