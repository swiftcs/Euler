def challenge2():
    counter = 1
    number1 = 1
    number2 = 1
    total = 0
    print(number1)
    while number2 < 400000000:
        fnum2 = number2
        fnum1 = number1
        number1 = fnum2
        number2 = fnum1 + fnum2
        if number2 % 2 == 0:
            print(number2)
            total = total + number2
    print("Total: ", total)