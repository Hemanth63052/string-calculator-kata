import re
# step 1
# step 2
def add(numbers_str: str) -> int:
    if not numbers_str:
        return 0
    actual_numbers = [int(each_num) for each_num in numbers_str.split(",")]
    return sum(actual_numbers)

assert add("1,5 , 6") == 12

