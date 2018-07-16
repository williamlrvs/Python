from abc import ABC
from collections.abc import MutableSequence
from numbers import Complex
from collections.abc import Sized
from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class Playlist(MutableSequence):
    pass

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

lista = MinhaListagem()
print(lista)

numeros = Numero()

filmes = Playlist()
