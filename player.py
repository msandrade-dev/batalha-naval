# game/player.py

# Classe que representa um jogador
class Player:
    def __init__(self, name, board):
        self.name = name      # Nome do jogador
        self.board = board    # Tabuleiro do jogador

    def attack(self, x, y, opponent_board):
        # Realiza um ataque no tabuleiro do oponente na posição (x, y)
        return opponent_board.receive_attack(x, y)

    def all_ships_sunk(self):
        # Verifica se todos os navios do jogador foram afundados
        return self.board.all_sunk()
