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
