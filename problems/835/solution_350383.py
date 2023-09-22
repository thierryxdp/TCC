def melhor_volta(matriz):
    """ Função que dada uma matriz com tempos de 6 corredores,
    em 10 voltas, retorna uma tupla informando de quem foi 
    a melhor volta da corrida, qual o melhor tempo dela,
    e em que volta tal fato aconteceu
    list -> tuple """
    lista_mins=[min(matriz[0]),min(matriz[1]),min(matriz[2]),min(matriz[3]),min(matriz[4]),min(matriz[5])]
    tempo=min(lista_mins)
    corredor=list.index(lista_mins,tempo)
    volta=list.index(matriz[corredor],tempo)
    return (corredor+1,tempo,volta+1)