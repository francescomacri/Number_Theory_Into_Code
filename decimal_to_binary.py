# decimal_to_binary.py

n = []


def decimal_to_binary_list(a):
    while a != 0:
        r = a % 2
        n.append(r)
        a = a // 2
    return n


def reverse_list_to_integer(n):
    reversed_string = "".join(str(element) for element in n[::-1])
    transformed = int(reversed_string)
    return transformed


def main():
    a = int(
        input("Please insert the decimal number you want to transform into binary: ")
    )
    print(
        f"{a} in binary notation is {reverse_list_to_integer(decimal_to_binary_list(a))}."
    )


if __name__ == "__main__":
    main()