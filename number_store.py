number_list = []
number_set = set()

def add_numbers(new_numbers: list[int]):
    for num in new_numbers:
        if num not in number_set:
            number_list.append(num)
            number_set.add(num)
#If duplicates are allowed, then just use the extend function: number_list.extend(new_numbers)

def get_all_numbers():
    return number_list

def get_average():
    if not number_list:
        return 0.0
    return sum(number_list) / len(number_list)

def get_count():
    return len(number_list)

def reset_numbers():
    number_list.clear()
