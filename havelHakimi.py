def remove_zeros(number_zeros):
    while 0 in number_zeros:
        number_zeros.remove(0)


def length_check(n, numbers):
    if n > len(numbers):
        return True
    else:
        return False


def front_elimination(n, numbers):
    for x in range(n):
        numbers[x] = numbers[x] - 1


def algorithm(numbers):
    print("New Sequence")
    n = 0

    # Remove Zeros
    remove_zeros(numbers)
    print(numbers)
    if len(numbers) == 0:
        return True

    # Sort
    numbers.sort(reverse=True)
    print(numbers)

    # Remove first answer
    n = numbers.pop(0)
    print(numbers)
    print("n = " + str(n))

    # Length check
    if length_check(n, numbers):
        return False

    # Subtract 1
    front_elimination(n, numbers)
    print(numbers)

    algorithm(numbers)


# Input
inputs = [16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]
print(inputs)

print(algorithm(inputs))
