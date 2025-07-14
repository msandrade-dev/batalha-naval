## 🚢 Batalha Naval em Python

Uma versão do clássico jogo *Batalha Naval* feita com **Python 3**, interface gráfica com **Tkinter**, efeitos sonoros com **pygame** e recursos visuais personalizados com **imagens temáticas**.

---

## 🎮 Como Jogar

1. Clique em 3 células do **seu tabuleiro** para posicionar seus navios.
2. Após posicioná-los, clique nas células do tabuleiro do **computador** para atacar.
3. Os acertos e erros são indicados por **sons** e **imagens**.
4. O jogo termina quando todos os navios de um jogador forem afundados.

---

## 📁 Estrutura do Projeto

batalha-naval/

├── main.py # Arquivo principal para executar o jogo

├── README.md

├── game/ # Módulo do jogo (código-fonte)

│ ├── init.py

│ ├── cell_state.py # Estados das células

│ ├── ship.py # Classe Ship

│ ├── board.py # Classe Board

│ ├── player.py # Classe Player

│ └── game_gui.py # Interface gráfica e lógica do jogo

├── assets/ # Imagens (64x64 PNG)

│ ├── water.png

│ ├── miss.png

│ ├── hit.png

│ ├── ship.png

│ └── ship_destroyed.png

├── sounds/ # Arquivos de som (WAV)

│ ├── hit.wav

│ ├── miss.wav

│ ├── win.wav

│ └── lose.wav


---

## ▶️ Como Executar

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/batalha-naval.git
cd batalha-naval

2. Crie um ambiente virtual (recomendado)

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows

3. Instale as dependências

pip install pygame
Obs: tkinter geralmente já vem com o Python. Se estiver usando Linux e não tiver o tkinter instalado, rode:
sudo apt install python3-tk

4. Execute o jogo

python main.py

---

## 🔊 Sons

Os sons estão localizados na pasta sounds/ e são reproduzidos via pygame.

| Ação    | Arquivo    |
| ------- | ---------- |
| Acerto  | `hit.wav`  |
| Erro    | `miss.wav` |
| Vitória | `win.wav`  |
| Derrota | `lose.wav` |

---

## 🖼️ Imagens

As imagens do jogo estão em assets/ e têm resolução 64x64.

| Nome do Arquivo      | Descrição                   |
| -------------------- | --------------------------- |
| `water.png`          | Células não atacadas (água) |
| `miss.png`           | Células atacadas sem acerto |
| `hit.png`            | Células com navio atingido  |
| `ship.png`           | Navio do jogador            |
| `ship_destroyed.png` | Navio do jogador atingido   |

---

## ✅ Funcionalidades

- Interface gráfica com botões clicáveis
- Sons e imagens para cada evento
- Posicionamento manual de navios do jogador
- Posicionamento aleatório da IA
- Turnos alternados entre jogador e computador
- Reinício rápido de partida com 1 clique

---

## 📌 Melhorias Futuras (sugestões)

- Animações ou transições com Canvas ou GIF
- Visualização de navios destruídos
- Indicação de navios restantes
- Diferentes configurações de navios (estratégia)
- Placar com estatísticas da partida
- Modo multiplayer local

---

## 👨‍💻 Autor

Márcio Santos Andrade
Desenvolvido como parte de projeto acadêmico na UFBA.

---

## 📝 Licença

Código aberto para fins educacionais e de uso livre.
