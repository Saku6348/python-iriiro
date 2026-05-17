def fizz_buzz(n,x,y,):
    if (n%x==0)and(n%y==0):
        st="FizzBuzz"
    elif n%x==0:
        st="Fizz"
    elif n%y==0:
        st="Buzz"
    else:
        st=str(n)
    return st

s=input("割りたい数を入力してください。")
r=input("割る数を入力してください。")
w=input("割る数を入力してください。")
print(fizz_buzz(int(s),int(r),int(w)))

    