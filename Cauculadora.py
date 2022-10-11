def soma(x,y):
    res = x+y
    print(res)

def sub(x,y):
    res = x-y
    print(res)

def multi(x,y):
    res = x*y
    print(res)

def div(x,y):
    res = x/y
    print(res)
valor1 = float(input("Digite o primeiro numero: "))
valor2 = float(input("Digite o segundo numero: "))

num1 = valor1
num2 = valor2
ope1 = str(input("Qual operação deseja: "))

match ope1:
    case "+":
        print(soma(num1,num2))
    case "-":
        print(sub(num1,num2))
    case "x":
        print(multi(num1,num2))
    case "/":
        print(div(num1,num2))