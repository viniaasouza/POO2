class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Duração: {self.duracao} - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Temporadas: {self.temporadas} - Likes: {self.likes}'

class Playlist(list):
    def __init__(self, nome, programa):
        self.nome = nome
        self.programa = programa

    def __getitem__(self, item):
        return self.programa[item]

    def __len__(self):
        return len(self.programa)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

print(f'Tamanho: {len(minha_playlist.listagem)}')

for programa in minha_playlist:
    print(programa)


#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} ' f'- duração: {vingadores.duracao}min'
#     f' Likes: {vingadores.likes}')
