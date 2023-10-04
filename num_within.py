def num_within(target, start, end):
    return target in range(start, end +1)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))