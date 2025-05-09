number_list = []

def add_numbers(new_numbers: list[int]):
    number_list.extend(new_numbers)

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
