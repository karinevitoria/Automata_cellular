import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- PARÂMETROS DA SIMULAÇÃO ---
GRID_SIZE = 100
INTERVAL = 50  # Milissegundos entre frames
GENERATIONS = 300 # Aumentei as gerações para uma análise melhor

# --- BANCO DE PADRÕES CLÁSSICOS ---

def get_pattern(name):
    """Retorna a matriz de um padrão famoso."""
    if name.lower() == 'gosper_glider_gun':
        return np.array([
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ], dtype=int)
    elif name.lower() == 'pulsar':
        return np.array([
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0]
        ], dtype=int)
    else: # Padrão 'random'
        return np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE), p=[0.8, 0.2])

def add_pattern(grid, pattern_name, position=(10, 10)):
    """Adiciona um padrão à grade em uma posição específica."""
    pattern = get_pattern(pattern_name)
    p_height, p_width = pattern.shape
    x, y = position
    
    # Garante que o padrão caiba na grade
    if x + p_height < GRID_SIZE and y + p_width < GRID_SIZE:
        grid[x:x+p_height, y:y+p_width] = pattern
    return grid

def update(frame, grid, im, ax, live_cell_density_data):
    """Função de atualização para a animação."""
    new_grid = grid.copy()
    
    neighbors = (
        np.roll(np.roll(grid, 1, 1), 1, 0) + np.roll(grid, 1, 0) +
        np.roll(np.roll(grid, -1, 1), 1, 0) + np.roll(grid, 1, 1) +
        np.roll(grid, -1, 1) + np.roll(np.roll(grid, 1, 1), -1, 0) +
        np.roll(grid, -1, 0) + np.roll(np.roll(grid, -1, 1), -1, 0)
    )

    birth = (neighbors == 3) & (grid == 0)
    survive = ((neighbors == 2) | (neighbors == 3)) & (grid == 1)
    
    new_grid[:] = 0
    new_grid[birth | survive] = 1
    
    grid[:] = new_grid[:]
    im.set_array(grid)
    
    # *** NOVA FUNCIONALIDADE: CÁLCULO DA DENSIDADE ***
    live_cells = np.sum(grid)
    total_cells = GRID_SIZE * GRID_SIZE
    density = (live_cells / total_cells) * 100
    live_cell_density_data.append(density)
    
    ax.set_title(f"Jogo da Vida - Geração {frame + 1} | Densidade: {density:.2f}%")
    return [im]

# *** NOVA FUNCIONALIDADE: GRÁFICO DE ANÁLISE ***
def plot_density_curve(density_data):
    """Plota a curva de densidade de células vivas ao longo do tempo."""
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(density_data)), density_data, color='blue')
    plt.title("Análise Quantitativa: Densidade de Células Vivas por Geração")
    plt.xlabel("Geração (Tempo)")
    plt.ylabel("Densidade de Células Vivas (%)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("density_analysis.png")
    print("Gráfico 'density_analysis.png' salvo.")
    plt.show()

# --- Script Principal ---
if __name__ == '__main__':
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    
    # --- ESCOLHA SEU CENÁRIO INICIAL AQUI ---
    # Descomente a linha que deseja usar
    grid = add_pattern(grid, 'gosper_glider_gun', position=(10, 5))
    # grid = add_pattern(grid, 'pulsar', position=(40, 40))
    # grid = get_pattern('random') # Para um início aleatório
    
    # Lista para guardar os dados de densidade
    live_cell_density_data = []

    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(grid, cmap='binary')
    ax.set_xticks([]); ax.set_yticks([])

    ani = FuncAnimation(fig, update, fargs=(grid, im, ax, live_cell_density_data),
                        frames=GENERATIONS, interval=INTERVAL, blit=True, repeat=False)
    
    print("Iniciando simulação e salvando animação... Isso pode levar um momento.")
    ani.save('game_of_life_simulation.gif', writer='pillow', fps=20)
    print("Animação 'game_of_life_simulation.gif' salva.")
    
    plt.show() # Mostra a animação

    # Ao final, plota e salva o gráfico de análise de densidade
    plot_density_curve(live_cell_density_data)