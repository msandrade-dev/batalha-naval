# main.py

# Importa a classe Tk da biblioteca tkinter para criar a janela principal da GUI
from tkinter import Tk
# Importa a classe GameGUI que gerencia a interface do jogo
from game.game_gui import GameGUI
# Importa a classe Player que representa um jogador (humano ou computador)
from game.player import Player
# Importa a classe Board que representa o tabuleiro do jogador
from game.board import Board

def main():
    # Cria a janela principal da aplicação
    root = Tk()
    # Cria o jogador humano com um novo tabuleiro
    player = Player("Jogador", Board("Jogador"))
    # Cria o jogador computador com um novo tabuleiro
    computer = Player("Computador", Board("Computador"))
    # Inicializa a interface do jogo com os dois jogadores
    game = GameGUI(root, player, computer)
    # Inicia o loop principal da aplicação Tkinter (mantém a janela aberta)
    root.mainloop()

# Garante que o main() será executado apenas quando o script for rodado diretamente
if __name__ == "__main__":
    main()
