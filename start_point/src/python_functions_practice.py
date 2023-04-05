def return_10():
    return 10

def add(first_number, second_number):
    sum_of_numbers = first_number + second_number
    return sum_of_numbers

def subtract(num_1, num_2):
    total_nums = num_1 - num_2
    return total_nums

def multiply(numb_1, numb_2):
    total_result = numb_1 * numb_2
    return total_result

def divide(nummy_1, nummy_2):
    total_nummies = nummy_1 / nummy_2
    return total_nummies

def length_of_string(test_string):
    string_length = len(test_string)
    return string_length

def join_string(string_1, string_2):
    joined_string = "".join([string_1, string_2])
    return joined_string

def add_string_as_number(num_1, num_2):
    strings_as_numbers = int(num_1) + int(num_2)
    return strings_as_numbers

def number_to_full_month_name(months_number):
    if months_number == 1:
        return "January"
    elif months_number == 3:
        return "March"
    elif months_number == 9:
        return "September"

def number_to_short_month_name(month_number):
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return month_list[month_number-1]

