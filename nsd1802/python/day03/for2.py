# range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(10))
# range(6, 11)  # [6, 7, 8, 9, 10]
# range(1, 10, 2)  # [1, 3, 5, 7, 9]
# range(10, 0, -1)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sum100 = 0

for i in range(1, 101):
    sum100 += i

print(sum100)