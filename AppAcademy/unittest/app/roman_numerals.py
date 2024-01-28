# def parse(roman_numeral):
#     # Implement logic to parse the roman numeral string and return the integer value
#     # Use loops, conditional statements, and dictionaries to handle different numerals and combinations
#     # Start with simple logic for handling 'I', 'II', and 'III', then gradually expand for other cases
#     # Refer to the provided rules and test cases for guidance

#     value = 0
#     for char in roman_numeral:
#         if char == "I":
#             value += 1
#         elif char == "V":
#             value += 5
#         elif char == "VI":
#             value += 6
#         elif char == "VII":
#             value += 7
#         elif char == "X":
#             value += 10 
#         elif char == "L":
#             value += 50
#         elif char == "100":
#             value += 100
#         elif char == "D":
#             value += 500
#         elif char == "M":
#             value += 1000
#     if "IV" in roman_numeral:
#         value -= 2
#     if "IX" in roman_numeral:
#         value -= 2
#     return value


def parse(roman_numeral):
    """Parses a Roman numeral string and returns its integer value."""

    num_map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    value = 0
    prev_value = 0
    for char in roman_numeral:
        current_value = num_map[char]

        if current_value > prev_value:
            value += current_value - 2 * prev_value
        else:
            value += current_value

        prev_value = current_value

    return value
