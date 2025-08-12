# Jogo da Vida de Conway: Simulação Avançada com Análise Quantitativa

Este projeto é uma implementação avançada do "Jogo da Vida" de John Conway, desenvolvida para a disciplina de Autômatos Celulares. O objetivo é não apenas visualizar a beleza dos padrões emergentes, mas também analisar quantitativamente a dinâmica do sistema.

O simulador é construído em Python, `NumPy` e `Matplotlib`, com foco em eficiência e análise de resultados.

## ✨ Funcionalidades "Next Level"

- **Visualização Dinâmica:** Gera uma animação em GIF de alta qualidade da evolução do autômato.
- **Análise Quantitativa:** Plota e salva um gráfico da **densidade de células vivas (%)** por geração, permitindo uma análise real do comportamento do sistema.
- **Banco de Padrões:** Inclui uma biblioteca de padrões iniciais clássicos, como a **Gosper Glider Gun**, **Pulsar**, e um modo **aleatório** para testar a emergência de ordem a partir do caos.

## 🔬 Resultados Gerados

Ao executar o script, três arquivos principais são gerados:

1.  **`game_of_life_simulation.gif`**: A animação da simulação.
    ![Animação da Simulação](results/game_of_life_simulation.gif)

2.  **`density_analysis.png`**: O gráfico de análise quantitativa.
    ![Gráfico de Densidade](results/density_analysis.png)

## 🚀 Como Executar

### Pré-requisitos

É necessário ter Python 3 instalado, juntamente com as bibliotecas: `numpy`, `matplotlib`, `pillow`.

```bash
pip install numpy matplotlib pillow