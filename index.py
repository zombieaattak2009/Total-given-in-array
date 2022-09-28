
def search(list, number):
    for i in range(len(list)):
        if list[i] == number:
            return True
    return False

def check(list, sum):
    for i in range(len(list)):
        if list[i] == sum:
            print(list[i])
            return True
    return False

n=input()
n=int(n)
total=input()
total=int(total)
a = list(range(1,n))
b = a[0]+a[1]+a[2]
c = total-b


if check(a, total):
    print("Found in array (No Calculations Done)")
    exit()
else:
    None


if search(a, c):
    answer=b+c
    print(a[0],"+",a[1],"+",a[2])
    print(total,"-",b)
    print(b,"+",c)
    print(answer)
else: 
    print("false")
    print("-1")





