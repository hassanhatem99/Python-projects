
def main():
    n = get_int("Enter Number: ")
    c = n
    sum = 0
    sum2 = 0

    # AMEX
    # if n starts with 34 or 37 and n has 15 digits

    if (c // 100000000000000) % 10 == 3 and (c // 10000000000000) % 10 == 7 and c // 1000000000000000 == 0:

        # sum for digits multiplied by 2
        i = 0
        while i < 7:
            digit = (n // 10) % 10
            n //= 100
            sum += (2 * digit) % 10 + (2 * digit) // 10
            i += 1

        # sum for digits not multiplied by 2
        n = c
        i = 0
        while i < 8:
            digit2 = n % 10
            n //= 100
            sum2 += digit2
            i += 1

        # check validity
        if (sum + sum2) % 10 == 0:
            print("AMEX")
        else:
            print("INVALID")

    # MASTERCARD
    # else if n starts with 51, 52, 53, 54, or 55 and n has 16 digits
    elif (c // 1000000000000000) % 10 == 5 and (c // 100000000000000) % 10 >= 1 and (c // 100000000000000) % 10 <= 5 and c // 10000000000000000 == 0:

        # sum for digits multiplied by 2
        i = 0
        while i < 8:
            digit = (n // 10) % 10
            n //= 100
            sum += (2 * digit) % 10 + (2 * digit) // 10

            i += 1

        # sum for digits not multiplied by 2
        n = c
        i = 0
        while i < 8:
            digit2 = n % 10
            n //= 100
            sum2 += digit2
            i += 1

        # check validity
        if (sum + sum2) % 10 == 0:

            print("MASTERCARD")
        else:
            print("INVALID")

    # VISA
    # else if n starts with 4 and n has 13 or 16 digits

    # 16-digit VISA
    elif (c // 1000000000000000) % 10 == 4 and (c // 10000000000000000 == 0):

        # sum for digits multiplied by 2
        i = 0
        while i < 8:
            digit = (n // 10) % 10
            n //= 100
            sum += (2 * digit) % 10 + (2 * digit) // 10
            i += 1

        # sum for digits not multiplied by 2
        n = c
        i = 0
        while i < 8:
            digit2 = n % 10
            n //= 100
            sum2 += digit2
            i += 1

        # check validity
        if (sum + sum2) % 10 == 0:
            print("VISA")
        else:
            print("INVALID")

    # 13-digit VISA
    elif (c // 1000000000000) % 10 == 4 and c // 10000000000000 == 0:

        # sum for digits multiplied by 2
        i = 0
        while i < 6:
            digit = (n // 10) % 10
            n //= 100
            sum += (2 * digit) % 10 + (2 * digit) // 10
            i += 1

        # sum for digits not multiplied by 2
        n = c
        i = 0
        while i < 7:
            digit2 = n % 10
            n //= 100
            sum2 += digit2
            i += 1

        # check validity
        if (sum + sum2) % 10 == 0:

            print("VISA")
        else:
            print("INVALID")

    else:
        print("INVALID")

    print()


def get_int(question):
    while True:
        n = input(f"{question}")
        try:
            n = eval(n)
            if n != int(n) or n < 0:
                print("Please type a positive integer")
                continue
            break
        except:
            print("Please type a number")
    return n


main()

