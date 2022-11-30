from calculadora import Calculadora 

calculo = None
while calculo !='s':
    calculo = input('Digite s para sair ou: \n digite c para continuar: \n')
    if calculo == 'c':
        c = Calculadora()
        a = int(input('digite primeiro numero: \n'))
        b = int(input('Digite segundo numero: \n'))
        op = str(input('Digite um OP: \n'))
        if op == '+':
            resultado = c.somar(a, b)
            print(f'resultado e: {resultado}')
        elif op == '-':
            resultado = c.subtrair(a, b)
            print(f"resultado e : {resultado}")
        elif op == '*':
            resultado = c.multiplicar(a, b)
            print(f"resultado {resultado}")
        elif op == '/':
            resultado = c.dividir(a, b)(a, b)
            print(f"resultado {resultado}")
        else :
            print("Operacao invalida") 
      