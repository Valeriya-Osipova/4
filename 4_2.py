def calc(main):
    while True:
        oper = input()
        def plus():
            a = float(input())
            b = float(input())
            c = a + b
            print(str(c))   
        def minus():
            a = float(input())
            b = float(input())
            c = a - b
            print(str(c))
        def umn():
            a = float(input())
            b = float(input())
            c = a * b
            print(str(c))
        def delenie():
            a = float(input())
            b = float(input())
            c = a / b
            print(str(c))
        if oper == "+":
            plus()
        elif oper == "-":
            minus()
        elif oper == "*":
            umn()
        elif oper == "/":
            delenie()
        elif oper == "q":
            break
oper = input()
calc(oper)