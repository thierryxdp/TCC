def melhor_volta(matriz):
    """ Função que dada uma matriz de 6 corredores e seus respectivos tempos em 10 voltas, retorna uma tupla informando de quem foi a melhor volta, qual o tempo e em que volta
    list -> tuple """
    lista_mins=[min(matriz[0]),min(matriz[1]),min(matriz[2]),min(matriz[3]),min(matriz[4]),min(matriz[5])]
    tempo=min(lista_mins)
    corredor=list.index(lista_mins,tempo)
    volta=list.index(matriz[corredor],tempo)
    return (corredor+1,tempo,volta+1)