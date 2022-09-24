

n=input()
n=int(n)
total=input()
total=int(total)
a = list(range(1,n))
b = a[0]+a[1]+a[2]
c = total-b

for i in range(len(a)):
    if a[i] == c:
        print("Found")
        answer=b+c
        break

print(answer)


