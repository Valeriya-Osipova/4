def calc(main):
    while True:
        oper = input()
        def plus():
            try:
                a = float(input())
                b = float(input())
                c = a + b
                print(str(c)) 
            except ValueError:
                print('неккоректно введены данные')  
        def minus():
            try:
                a = float(input())
                b = float(input())
                c = a - b
                print(str(c)) 
            except ValueError:
                print('неккоректно введены данные')  
        def umn():
            try:
                a = float(input())
                b = float(input())
                c = a * b
                print(str(c)) 
            except ValueError:
                print('неккоректно введены данные')  
        def delenie():
            try:
                a = float(input())
                b = float(input())
                c = a / b
                print(str(c)) 
            except ValueError:
                print('неккоректно введены данные')  
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