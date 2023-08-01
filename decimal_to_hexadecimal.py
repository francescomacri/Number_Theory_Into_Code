# decimal_to_hexadecimal.py

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return "0"

    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(65 + remainder - 10) + hexadecimal
        decimal //= 16

    return hexadecimal


def main():
    a = int(
        input(
            "Please insert the decimal number you want to transform into hexadecimal: "
        )
    )
    print(f"{a} in hexadecimal notation is {decimal_to_hexadecimal(a)}.")


if __name__ == "__main__":
    main()