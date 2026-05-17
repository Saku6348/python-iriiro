def fizz_buzz(n):
    print(str(n))
    if n%15==0:
        st="FIzzBuzz"
    elif n%3==0:
        st="Fizz"
    elif n%5==0:
        st="Buzz"
    else:
        st=str(n)
    return st

sizensuu=input("自然数を入力してください。")
print(fizz_buzz(int(sizensuu)))

    