class CalcCubo:
    '''Classe para calcula o cubo de um número'''
    def __init__(self, valor):  # esse é o metodo construtor, ele é uma definicição
        self.x = valor          # perceba tambem que ele sempre inicia com "self"
        print('objeto criado')
    # NOTA: dêntro da classe nós criamos varios metodos, no caso agora vamos criar
    # um metodo para fazer o cálculo...

    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return f'cubo calculado: {cubo}'


num = int(input('entre com um numero: '))
objCubo = CalcCubo(num)  # iniciar a classe
cubo = objCubo.calcula_cubo()  # o metodo calcula cubo está associado ao "objCubo"
print(cubo)
print(type(CalcCubo))  # <class 'type'>
print(type(objCubo))  # <class '__main__.CalcCubo'> isso está mostrando que
                      # foi derivado de "CalcCubo"

# podemos estanciar varios objetos e todos podem ter valores diferentes
num = int(input('entre com um numero: '))
objCubo2 = CalcCubo(num)
cubo2 = objCubo2.calcula_cubo()
print(cubo2)
print(type(CalcCubo))
print(type(objCubo))

