def melhor_volta (matriz):
    """Função que recebe uma matriz 6x10 com os tempos dos corredores e retorna de quem foi a melhor volta, com qual tempo e em que volta;
       list -> tuple."""
    lista_menores= []
    i= 0
    j=0
    for lista in matriz:
        menor = min (lista)
        lista_menores = lista_menores + [menor]
    melhor_tempo = min (lista_menores)
    corredor = list.index (lista_menores, melhor_tempo)
    volta= list.index (matriz[corredor],melhor_tempo)
    return (corredor + 1, melhor_tempo, volta +1)