def melhor_volta(matriz):
    """Funcao recebe uma matriz 6x10 dada: matriz com os tempos em segundos
    dos corredores de kart e retorna uma tupla, dizendo de quem foi a melhor
    volta da prova, com qual tempo e em que volta """
    
    piloto = 1

    volta = 1

    tempo = matriz[0][0]

    resultado = ()
    
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] < tempo:
                piloto = linha+1
                volta = coluna+1
                tempo = matriz[linha][coluna]

    return resultado + (piloto, tempo, volta, )