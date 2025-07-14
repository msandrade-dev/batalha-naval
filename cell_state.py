# game/cell_state.py

# Define os possíveis estados de uma célula do tabuleiro
class CellState:
    EMPTY = " "  # Célula vazia
    SHIP = "S"    # Célula com navio
    HIT = "X"     # Célula com navio atingido
    MISS = "O"    # Célula onde o ataque errou
