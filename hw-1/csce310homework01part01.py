import sys


def productOfDigits(number):
    product = 1
    digits = [int(d) for d in str(int(number))]

    for digit in digits:
        product = product * digit

    return product


if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    numTxt = file.readline()
    number = float(numTxt)
    print(
        "The product of the digits in {} is {}".format(numTxt, productOfDigits(number))
    )
