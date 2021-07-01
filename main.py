def happy_number(n):
    result = 0
    while n>0:
        first=n%10
        result=result+(first*first)
        n=n//10
    return result


n=int(input("enter a number"))
result=n
seen = set()


while result not in seen:
    a=result
    seen.add(a)
    # print(seen)
    if result == 1:
        print(n, "is a happy number")
        break
    result=happy_number(result)
else:
    print(n,"is not a happy number")


