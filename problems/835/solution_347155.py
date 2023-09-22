def melhor_volta(matriz):
    '''função que recebe uma matriz contendo os tempos que cada um dos 6 corredores obtiveram em cada uma das 10 voltas,
e retorna de quem foi a melhor volta, com qual tempo e em que volta, respectivamente.
list(list) -> tuple(int,float,int)'''
    lista = []
    pos_lista = 0
    contador = 0
    while pos_lista < len(matriz):
        for i in range(len(matriz[pos_lista])):
            list.append(lista,matriz[pos_lista][i])
        pos_lista = pos_lista + 1
    tempo = min(lista)
    while contador < len(matriz):
        if tempo in matriz[contador]:
            corredor = contador
            volta = list.index(matriz[contador],tempo)
        contador = contador + 1
    tupla = corredor+1,tempo,volta+1
    return tupla