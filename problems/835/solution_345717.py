def melhor_volta(matriz):
    """Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em 
    cada volta, retornando uma tupla informando quem fez a melhor volta, com qual tempo
    e em que volta
    entrada: list(list)
    retorno: tuple(int, int, int)"""
    tempo = 0
    t_ant = 0
    for i in range(len(matriz)):
        if tempo == 0:
            volta = matriz[i].index(min(matriz[i])+1
            tempo = min(matriz[i])
            piloto = i + 1
        if min(matriz[i]) < t_ant:
            volta = matriz[i].index(min(matriz[i])+1
            tempo = min(matriz[i])
            piloto = i + 1
        t_ant = min(matriz[i])
     return (piloto, tempo, volta)