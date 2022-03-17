def number_length(num):
    string_num = str(num)
    return 1 + number_length(string_num[1:]) if string_num else 0
