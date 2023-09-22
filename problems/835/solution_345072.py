def melhor_volta(matriz):
    """Função que recebe o tempo de 6 corredores em cada uma das 10 voltas e retorna quem fez a melhor volta, 
    com qual tempo e em que volta"""
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(lista, matriz[i][j])
    tempo = min(lista)
    corredor = list.index(matriz, tempo) + 1
    volta = list.index(matriz[corredor], tempo) + 1
    return (corredor, tempo, volta)