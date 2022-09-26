
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
    exit()
else:
    None


if search(a, c):
    print("True")
    answer=b+c
    print(answer)
else: 
    print("false")
    print("-1")





