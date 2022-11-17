class NomeClase01:  # cabeçalho da classe
    pass  # classe sem nehuma função (ainda...)


print(type(NomeClase01))  # classe do elemento


class Cubo:
    '''Classe para calcula o cubo de um número'''
    def __init__(self, valor):  # esse é o metodo construtor, ele é uma definicição
        self.x = valor          # perceba tambem que ele sempre inicia com "self"
        print('objeto criado')
    # NOTA: dêntro da classe nós criamos varios metodos, no caso agora vamos criar
    # um metodo para fazer o cálculo...
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return f'cubo calculado: {cubo}'


teste = Cubo(6)
# isso vai criar um objeto chamado "teste" o parametro "6" esta sendo passado
# como parametro dêntro da classe "cubo", perceba que ele chama apenas a primeira
# construção caso querira chamar outra função deve fazer a requisição como a baixo
c = teste.calcula_cubo()
print(c)

