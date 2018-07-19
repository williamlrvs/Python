from tabuleiro import board

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.letra_certa = []
        self.letra_errada = []

    # Método para adivinhar a letra
    def guess(self,letra):
        if letra in self.word and letra not in self.letra_certa:
            self.letra_certa.append(letra)
        elif letra not in self.word and letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False

        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letra_errada) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if "_" not in self.hide_word():
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        palavra_secreta = ""
        for letra in self.word:
            if letra not in self.letra_certa:
                palavra_secreta += "_ "
            else:
                palavra_secreta += letra

        return palavra_secreta

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.letra_errada)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', )
        for letter in self.letra_errada:
            print(letter, )
        print()
        print('Letras corretas: ', )
        for letter in self.letra_certa:
            print(letter, )

def mensagem_fim_do_jogo(game):
    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + str(game.word).upper())
    print('\nFoi bom jogar com você! Agora vá estudar!\n')


def motor_do_jogo(game):
    game.print_game_status()
    user_input = input('\nDigite uma letra: ').lower()
    game.guess(user_input)