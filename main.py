class Calculadora :
    def __init__(self, a= None, b = None, op = None):
        self.a = a
        self.op = op
        self.b = b 

    def somar(self):
        self.a = int(input('digite primeiro numero: \n'))
        self.op = str(input('Digite um OP: \n'))
        self.b = int(input('Digite segundo numero: \n'))
        if self.op == '+':
            resultado = self.a + self.b
            print(f'resultado e: {resultado}')
        if self.op == '-':
            resultado = self.a - self.b 
            print(f"resultado e : {resultado}")
        if self.op == '*':
            resultado = self.a * self.b 
            print(f"resultado {resultado}")
        else :
            print("Operacao invalida")     

calculo = None
while calculo !='s':
    calculo = input('Digite s para sair ou: \n digite c para continuar: \n')
    if calculo == 'c':
       c = Calculadora().somar()
      