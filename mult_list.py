def mult_list(list):
    if len(list) == 0:
        return 0
    prod = list[0]
    if len(list) > 1:
        for num in list[1:]:
            prod = prod * num
    return prod

print(mult_list([1, 2, 3]))
print(mult_list([1, 2, 3, 4, 5, 6]))
print(mult_list([]))
print(mult_list([5]))