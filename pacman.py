if __name__ == '__main__':
    from random import randint
    import os
    from time import sleep

    TAMANHO_GRID = 10 # Tamanho do grid do jogo
    PACMAN = ['O', 'o']  # Lista com as formas do pacman a cada interação
    COMIDA = 'X' # Formato da comida
    TEMPO_DA_INTERACAO = 0.5  # Tempo entre as interações de movimento do pacman

    pos_pacman = [randint(0, TAMANHO_GRID - 1), randint(0, TAMANHO_GRID - 1)] # Sortear posição que o pacman vai ficar no jogo
    pos_comida = [randint(0, TAMANHO_GRID - 1), randint(0, TAMANHO_GRID - 1)] # Sortear posição que vai ficar a comida no jogo

    pacman_formato = PACMAN[0] # Formato do primeiro pacman no jogo

    # Imprimindo o jogo na tela
    def imprimir_grid():
        os.system('cls')
        for l in range(TAMANHO_GRID): # percorre as linhas do jogo - índice [0]
            for c in range(TAMANHO_GRID): # percorre as colunas do jogo - índice [1]
                if l == pos_pacman[0] and c == pos_pacman[1]:
                    print(pacman_formato, end='')  # Imprime a forma atual do Pacman no grid
                elif l == pos_comida[0] and c == pos_comida[1]:
                    print(COMIDA, end='') # Imprime a comida do grid
                else:
                    print('.', end='')
            print()

    # Função para mover o Pacman em direção à comida
    def mover_pacman():
        if pos_pacman[0] < pos_comida[0]:
            pos_pacman[0] += 1
        elif pos_pacman[0] > pos_comida[0]:
            pos_pacman[0] -= 1
        elif pos_pacman[1] < pos_comida[1]:
            pos_pacman[1] += 1
        elif pos_pacman[1] > pos_comida[1]:
            pos_pacman[1] -= 1

    # Loop principal do jogo
    while True:
        imprimir_grid()
        mover_pacman()

        # Altera a forma do Pacman para a próxima forma na lista
        pacman_formato = PACMAN[(PACMAN.index(pacman_formato) + 1) % len(PACMAN)]

        if pos_pacman == pos_comida:
            pos_comida = [randint(0, TAMANHO_GRID - 1), randint(0, TAMANHO_GRID - 1)]
        sleep(TEMPO_DA_INTERACAO)