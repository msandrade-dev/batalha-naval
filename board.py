# game/board.py

# Importa o módulo random para geração de posições aleatórias
import random
# Importa os estados possíveis de uma célula no tabuleiro
from .cell_state import CellState
# Importa a classe Ship que representa um navio no jogo
from .ship import Ship

# Define o tamanho do tabuleiro
BOARD_SIZE = 5
# Define a quantidade de navios por jogador
SHIP_COUNT = 3

class Board:
    def __init__(self, owner):
        # Nome do dono do tabuleiro (jogador ou computador)
        self.owner = owner
        # Cria uma grade do tabuleiro preenchida com células vazias
        self.grid = [[CellState.EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        # Lista para armazenar os navios posicionados
        self.ships = []

    def place_ship(self, x, y):
        # Coloca um navio na posição (x, y) se estiver vazia
        if self.grid[x][y] == CellState.EMPTY:
            ship = Ship((x, y))
            self.ships.append(ship)
            self.grid[x][y] = CellState.SHIP
            return True
        return False

    def place_ships_randomly(self):
        # Posiciona navios aleatoriamente até atingir SHIP_COUNT
        while len(self.ships) < SHIP_COUNT:
            x = random.randint(0, BOARD_SIZE - 1)
            y = random.randint(0, BOARD_SIZE - 1)
            self.place_ship(x, y)

    def receive_attack(self, x, y):
        # Trata um ataque na posição (x, y)
        for ship in self.ships:
            if (x, y) == ship.position:
                ship.register_hit((x, y))
                self.grid[x][y] = CellState.HIT
                return True
        self.grid[x][y] = CellState.MISS
        return False

    def all_sunk(self):
        # Verifica se todos os navios foram afundados
        return all(ship.is_sunk() for ship in self.ships)
