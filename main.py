

def add(numbers_str: str) -> int:
    if not numbers_str:
        return 0
    actual_numbers = [int(each_num) for each_num in numbers_str.split(",")]
    return sum(actual_numbers)

print(add("1,3,6,7"))