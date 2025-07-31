import re

def add(numbers_str: str) -> int:
    if not numbers_str:
        return 0
    actual_numbers = [int(each_num) for each_num in re.split(r"[,\n]", numbers_str)]
    return sum(actual_numbers)

assert add("1 \n 5 , 6") == 12