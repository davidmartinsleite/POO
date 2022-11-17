class Gato:
    def __init__(self, nome):  # veja que o termo "__init__" ele representa a inicialisão
        # do objeto aqui normalemente é criada a inicialização das variaveis internas
        self.nome = nome
        print('seu gato se chama: ', self.nome)

    def peso_gato(self, peso):
        self.peso = peso
        if self.peso > 5:
            print('seu gato esá gordinho')
        elif self.peso > 3.5:
            print('peso parace normal')
        else:
            print('o animal está abaixo do peso!')

    # aqui nos vamos definir um metodo utilitario privado
    def _dieta_especial_gato(self):  # repare o "_" no inico serve para evitar o uso
        self.msg = 'tudo ok!'
        if self.peso < 3.5:
            self.msg = 'aumente a ração do felino'
        if self.peso >= 5:
            self.msg = 'diminua a ração do felino'
        return self.msg
    # NOTA: esse metodo não tem acesso, logo vamos ter que criar um metodo
    # para dar acesso a esse metodo

    def dados_gato(self):
        print('o gato', self.nome, 'está com ', self.peso, 'kg')
        print(self._dieta_especial_gato())  # com essa chamada ele vai chamar o metodo privado


nome_gato = input('digite o nome de seu gato: ')
g1 = Gato(nome_gato)  # a classe "gato" foi estanciada, passa para "g1" o nome
# que estava dentro do metodo construtor, que vem automaticamente pelo "__init__"

peso = float(input('qual o peso do seu gato? '))
g1.peso_gato(peso)  # aqui nós chamamos a estancia "peso_gato"

g1.dados_gato()
