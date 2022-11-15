class Gato:
    tipo_animal = 'felino'  # esse valor e padrão para TODOS

    def __init__(self, nome):
        self.nome = nome


g1 = Gato('mia')
g2 = Gato('gibão')

print(g1.tipo_animal)  # o seu retorno é chamádo de valor de classe
print(g2.tipo_animal)

print(g1.nome)  # o seu retorno é uma variavel de instância
print(g2.nome)

# eu posso mudar os valores de classe acessando o mesmo e auterando
Gato.tipo_animal = 'pet'

print(g1.tipo_animal)  # perceba que o resultado agora e "pet"
print(g2.tipo_animal)

# aqui vamos auterar a variavel de classe se apenas no OBJETO
g1.tipo_animal = 'bichano'
print(g1.tipo_animal)  # perceba que vamos ter agora resultados diferentes para g1
print(g2.tipo_animal)
