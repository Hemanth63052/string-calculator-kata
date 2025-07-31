# step 1
# step 2
def add(numbers_str: str) -> int:
    if not numbers_str:
        return 0
    actual_numbers = [int(each_num) for each_num in numbers_str.split(",")]
    return sum(actual_numbers)

assert add("1,5 , 6") == 12

import re
# step 3
def add(numbers_str: str) -> int:
    if not numbers_str:
        return 0
    actual_numbers = [int(each_num) for each_num in re.split("[,\n]", numbers_str)]
    return sum(actual_numbers)

assert add("1\n5 , 6") == 12


def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [",", "\n"]

    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        custom_delimiter = delimiter_line[2:]
        delimiters = [custom_delimiter]

    pattern = "|".join(map(re.escape, delimiters))
    return sum(int(n) for n in re.split(pattern, numbers))

assert add("//;\n1;2") == 3
assert add("//#\n2#3#4") == 9

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [",", "\n"]

    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        custom_delimiter = delimiter_line[2:]
        delimiters = [custom_delimiter]

    pattern = "|".join(map(re.escape, delimiters))
    parts = re.split(pattern, numbers)
    values = []
    for each_num in parts:
        if each_num and int(each_num)>=0:
            values.append(int(each_num))
        else:
            raise ValueError(f"negative numbers not allowed: {each_num}")

    return sum(values)

assert add("1,2,3") == 6
assert add("//;\n4;5;6") == 15

try:
    add("1,-2,3,-4")
except ValueError as e:
    print(e)  # Output: negative numbers not allowed: -2,-4

