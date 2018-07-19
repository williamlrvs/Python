import random

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f: bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip().lower()
