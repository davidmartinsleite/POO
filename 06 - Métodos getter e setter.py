class Teste():
    def __init__(self, valor):
        self.x = valor

    def get_valor(self):
        '''metodo getter para retornar o vbalor do atributo x'''
        return self.x

    def set_valor (self, v):
        '''metodo setter para atribuir um novo valor ao atributo x'''
        self.x = v


teste = Teste(10)
print('valor do objeto: ', teste.get_valor())
# esse valor de 10 foi atribuido a classe Teste depois ele foi istanciado para get_valor

val = int(input('digite um valor numeroco: '))
teste.set_valor(val)  # aqui nos mudamos o valor do atributo x da classe Teste
print('valor do objeto após a atribuição: ', teste.get_valor())
# repare que o mesmo comando foi usado mais com o resultado agora diferente
