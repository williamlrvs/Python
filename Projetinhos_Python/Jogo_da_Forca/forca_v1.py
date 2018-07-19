# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
from Util import *
from Hangman import *

# Função Main - Execução do Programa
def main():

    # Criação do Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não estiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        motor_do_jogo(game)

    # Verifica o status do jogo
    game.print_game_status()

    mensagem_fim_do_jogo(game)

# Executa o programa
if __name__ == "__main__":
    main()
