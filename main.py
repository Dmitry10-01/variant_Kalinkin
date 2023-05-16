my_list = [4, 8, 2, 10, 3, 6]
max_value = max(my_list)
second_max = max(num for num in my_list if num != max_value)
print(second_max)
