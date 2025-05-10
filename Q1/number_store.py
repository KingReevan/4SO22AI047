WINDOW_SIZE = 10
number_list = []
number_set = set()

def add_numbers(new_numbers: list[int]):
    global number_list, number_set

    for num in new_numbers:
        if num not in number_set:
            if len(number_list) >= WINDOW_SIZE:
                # Remove the oldest number
                removed = number_list.pop(0)
                number_set.remove(removed)
            number_list.append(num)
            number_set.add(num)

def get_all_numbers():
    return number_list

def get_average():
    if not number_list:
        return 0.0
    return sum(number_list) / len(number_list)

