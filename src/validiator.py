# check the validity of credit card numbers


def add_num(num):
    if num < 10:
        return num
    else:
        sum = (num % 10) + (num // 10)
        return sum


def reverse_num(num):
    return num[ ::-1 ]


def double_second_num(num):
    doubled_second_digit_list = list()
    num_list = list(enumerate(num, start=1))

    for index, digit in num_list:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    return doubled_second_digit_list


def validate(cc_num):
    # reverse the credit card number
    cc_num_reversed = reverse_num(cc_num)

    # convert list to integers
    cc_num_reversed = [ int(num) for num in cc_num_reversed ]

    # double every second digit
    doubled_second_digit_list = double_second_num(cc_num_reversed)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [ add_num(num) for num in doubled_second_digit_list ]

    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)

    # return True or False
    if sum_of_digits % 10 == 0:
        return True
    else:
        return False
