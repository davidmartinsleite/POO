class Gato:
    def __init__(self, nome):  # veja que o termo "__init__" ele representa a inicialisão do objeto
        # aqui normalemente é criada a inicialização das variaveis internas
        self.nome = nome
        print('seu gato se chama: ', self.nome)


nome_gato = input('digite o nome de seu gato: ')
g1 = Gato(nome_gato)  # a classe "gato" foi estanciada, passa para "g1" o nome
# que estava dentro do metodo construtor, que vem automaticamente pelo "__init__"
