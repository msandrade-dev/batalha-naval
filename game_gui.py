# game/game_gui.py

# Importa o módulo tkinter para a criação da interface gráfica
import tkinter as tk
# Importa messagebox do tkinter para exibir mensagens ao usuário
from tkinter import messagebox
# Importa threading para execução de sons em paralelo sem travar a GUI
import threading
# Importa pygame para tocar sons
import pygame
# Importa random para gerar posições aleatórias no tabuleiro
import random
# Importa constantes e classes necessárias do módulo board
from .board import BOARD_SIZE, SHIP_COUNT, Board
# Importa os estados possíveis de uma célula
from .cell_state import CellState
# Importa a classe Player que representa cada jogador
from .player import Player

# Define a classe que gerencia toda a interface gráfica do jogo
class GameGUI:
    def __init__(self, root, player: Player, computer: Player):
        self.root = root  # Armazena a janela principal
        self.root.title("Batalha Naval")  # Define o título da janela
        self.original_player = player  # Guarda referência ao jogador original (não utilizado diretamente após refatoração)
        self.original_computer = computer  # Guarda referência ao computador original
        self.init_sounds()  # Inicializa os sons do jogo
        self.load_images()  # Carrega as imagens utilizadas no jogo
        self.init_game()  # Inicializa o estado do jogo

    def init_sounds(self):
        # Inicializa o mixer do pygame para tocar sons
        pygame.mixer.init()
        # Carrega os arquivos de som em um dicionário para acesso rápido
        self.sounds = {
            "hit": pygame.mixer.Sound("sounds/hit.wav"),
            "miss": pygame.mixer.Sound("sounds/miss.wav"),
            "win": pygame.mixer.Sound("sounds/win.wav"),
            "lose": pygame.mixer.Sound("sounds/lose.wav"),
        }

    def play_sound(self, name):
        # Reproduz o som em uma thread separada para não travar a GUI
        sound = self.sounds.get(name)
        if sound:
            threading.Thread(target=sound.play, daemon=True).start()

    def load_images(self):
        # Carrega as imagens dos elementos do tabuleiro e as armazena em um dicionário
        self.images = {
            "water": tk.PhotoImage(file="assets/water.png"),
            "miss": tk.PhotoImage(file="assets/miss.png"),
            "hit": tk.PhotoImage(file="assets/hit.png"),
            "ship": tk.PhotoImage(file="assets/ship.png"),
            "ship_destroyed": tk.PhotoImage(file="assets/ship_destroyed.png")
        }

    def init_game(self):
        # Recria os objetos Player e Board para reiniciar o estado do jogo
        self.player = Player("Jogador", Board("Jogador"))
        self.computer = Player("Computador", Board("Computador"))
        self.computer.board.place_ships_randomly()  # Posiciona navios aleatórios para o computador
        self.ship_placement_phase = True  # Indica que estamos na fase de posicionamento dos navios

        # Inicializa as matrizes de botões para os dois tabuleiros
        self.player_buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.computer_buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.player_ships_placed = 0  # Contador de navios posicionados pelo jogador

        # Remove todos os widgets da janela para reiniciar a interface
        for widget in self.root.winfo_children():
            widget.destroy()

        # Label de instruções para o jogador
        self.info_label = tk.Label(self.root, text="Clique em seu tabuleiro para posicionar 3 navios.")
        self.info_label.pack()

        # Cria o frame principal que conterá os tabuleiros
        board_frame = tk.Frame(self.root)
        board_frame.pack(pady=10)

        # Frame do tabuleiro do jogador
        self.player_frame = tk.LabelFrame(board_frame, text="Seu Tabuleiro")
        self.player_frame.grid(row=0, column=0, padx=10)

        # Frame do tabuleiro do computador
        self.computer_frame = tk.LabelFrame(board_frame, text="Ataque o Computador")
        self.computer_frame.grid(row=0, column=1, padx=10)

        # Constrói os botões de cada tabuleiro
        self.build_boards()

        # Botão para reiniciar o jogo
        self.reset_button = tk.Button(self.root, text="Reiniciar Jogo", command=self.init_game)
        self.reset_button.pack(pady=5)

    def build_boards(self):
        # Para cada célula dos tabuleiros, cria botões associados à função de clique
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # Botão do tabuleiro do jogador para posicionar navios
                btn_player = tk.Button(
                    self.player_frame, image=self.images["water"], width=64, height=64,
                    command=lambda x=i, y=j: self.place_player_ship(x, y) if self.ship_placement_phase else None
                )
                btn_player.grid(row=i, column=j)
                self.player_buttons[i][j] = btn_player

                # Botão do tabuleiro do computador para atacar posições
                btn_comp = tk.Button(
                    self.computer_frame, image=self.images["water"], width=64, height=64,
                    command=lambda x=i, y=j: self.player_attack(x, y) if not self.ship_placement_phase else None
                )
                btn_comp.grid(row=i, column=j)
                self.computer_buttons[i][j] = btn_comp

    def place_player_ship(self, x, y):
        # Tenta posicionar um navio na posição clicada
        if self.player.board.place_ship(x, y):
            # Atualiza imagem da célula para mostrar o navio
            self.player_buttons[x][y].config(image=self.images["ship"])
            self.player_ships_placed += 1
            # Se todos os navios foram posicionados, muda para fase de ataque
            if self.player_ships_placed == SHIP_COUNT:
                self.ship_placement_phase = False
                self.info_label['text'] = "Navios posicionados! Ataque o inimigo."
        else:
            # Caso a célula já tenha navio, avisa o jogador
            self.info_label['text'] = "Já há um navio aqui. Escolha outra célula."

    def player_attack(self, x, y):
        # Verifica se a célula já foi atacada
        cell = self.computer.board.grid[x][y]
        if cell in [CellState.HIT, CellState.MISS]:
            self.info_label['text'] = "Você já atacou aqui!"
            return

        # Realiza o ataque e obtém resultado
        hit = self.player.attack(x, y, self.computer.board)
        # Atualiza imagem da célula conforme o resultado
        btn = self.computer_buttons[x][y]
        btn.config(image=self.images["hit"] if hit else self.images["miss"])
        btn.config(state='disabled')  # Desativa botão para evitar novo clique
        self.play_sound("hit" if hit else "miss")  # Toca som apropriado

        # Verifica se o jogador venceu
        if self.computer.board.all_sunk():
            self.play_sound("win")
            messagebox.showinfo("Vitória", "Você venceu!")
            return

        # Passa o turno para o computador após um tempo
        self.root.after(1000, self.computer_turn)

    def computer_turn(self):
        # Executa ataque do computador de forma aleatória
        while True:
            x = random.randint(0, BOARD_SIZE - 1)
            y = random.randint(0, BOARD_SIZE - 1)
            if self.player.board.grid[x][y] in [CellState.EMPTY, CellState.SHIP]:
                hit = self.computer.attack(x, y, self.player.board)
                btn = self.player_buttons[x][y]
                # Atualiza imagem conforme o resultado
                if hit:
                    btn.config(image=self.images["ship_destroyed"])
                    self.play_sound("hit")
                else:
                    btn.config(image=self.images["miss"])
                    self.play_sound("miss")
                break

        # Verifica se o jogador perdeu
        if self.player.board.all_sunk():
            self.play_sound("lose")
            messagebox.showinfo("Derrota", "O computador venceu!")
