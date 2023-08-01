# euclidean_algorithmpypy

def euclid(a, b):
    while b != 0:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r
    return


def main():
    a = int(input("Integer a:"))
    b = int(input("Integer b:"))
    print(f"The gcd of {a} and {b} is {euclid(a, b)}.")


if __name__ == "__main__":
    main()