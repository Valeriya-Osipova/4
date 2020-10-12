#программа с рекурсией
def F(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)
print(F(6))


#программа с циклом
n = int(input())
a = 0
print(a)
b = 1
print(b)
c = 0
for i in range (0,n):
    c = a + b
    a = b
    b = c
    print(c)
