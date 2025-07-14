# game/ship.py

# Classe que representa um navio
class Ship:
    def __init__(self, position):
        self.position = position  # Posição do navio no tabuleiro
        self.hits = set()         # Conjunto para registrar se foi atingido

    def is_sunk(self):
        # Verifica se o navio foi afundado (atingido em sua única posição)
        return self.position in self.hits

    def register_hit(self, pos):
        # Registra um acerto se a posição do tiro for a do navio
        if pos == self.position:
            self.hits.add(pos)
            return True
        return False
