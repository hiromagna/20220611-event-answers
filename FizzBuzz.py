for num in range(1, 101):
    string = ''

    # ここから記述
    #3と5の最小公倍数となる15から先に処理する
    if(num%15==0):
        string += "FizzBuzz"
    elif(num%3==0):
        string += "Fizz"
    elif(num%5==0):
        string += "Buzz"
    else:
        string += str(num)


    # ここまで記述

    print(string)