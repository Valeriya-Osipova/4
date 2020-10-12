koord = []
for i in range(5):
    a = input().split()
    koord.append([int(a[0]),int(a[1])])

def side(x1,y1,x2,y2):
    lenght = ((x1-x2)**2+(y1-y2)**2)**0.5 
    return lenght

def geron(a, b, c):
    pp = (a+b+c)/2 
    s = (pp*(pp-a)*(pp-b)*(pp-c))**0.5
    return s

s = 0
a = side(koord[0][0],koord[0][1],koord[1][0],koord[1][1])
b = side(koord[1][0],koord[1][1],koord[2][0],koord[2][1]) 
c = side(koord[0][0],koord[0][1],koord[2][0],koord[2][1])
s += geron(a, b, c)

a = side(koord[0][0],koord[0][1],koord[2][0],koord[2][1]) 
b = side(koord[2][0],koord[2][1],koord[3][0],koord[3][1]) 
c = side(koord[0][0],koord[0][1],koord[3][0],koord[3][1]) 
s += geron(a, b, c)

a = side(koord[0][0],koord[0][1],koord[3][0],koord[3][1]) 
b = side(koord[3][0],koord[3][1],koord[4][0],koord[4][1]) 
c = side(koord[0][0],koord[0][1],koord[4][0],koord[4][1]) 
s += geron(a, b, c)
print(s)