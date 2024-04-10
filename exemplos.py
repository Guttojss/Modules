def subtrair(a,b):
    print(a-b)
def somar(a,b):
    print(a+b)
def dividir(a,b):
    print(a/b)
def multiplicar(a,b):
    print(a*b)

print("Qual operação deseja fazer?")

op=str(input("*(Multiplicação), -(Subtração), +(Soma) ou /(Divisão)"))

print("Quais são os numeros que deseja calcular?")

a=int(input("Primeiro numero : "))
b=int(input("Segundo numero :"))

match op:
    case '*':
         multiplicar(a,b)
    case '+':
        somar(a,b)
    case '-':
        subtrair(a,b)
    case '/':
        dividir(a,b)
    case _ : print("Insira uma opão válida")