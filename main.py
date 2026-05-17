def fizz_buzz(n):
    if n%15==0:
        str="FIzzBuzz"
    elif n%3==0:
        str="Fizz"
    elif n%5==0:
        str="Buzz"
    else:
        str=n
    return str

sizensuu=input("自然数を入力してください。")
print(fizz_buzz(int(sizensuu)))

    