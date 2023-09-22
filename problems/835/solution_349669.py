def melhor_volta(matriz):
    '''Função que, dada uma matriz 6x10 que representa os tempos das 10 voltas dos 6 pilotos de kart, retorna uma tupla contendo o corredor, o tempo e o número da melhor volta (a qual obteve o menor tempo), respectivamente.
list(list) --> tup'''
    linhas = len(matriz)
    lista1 = []
    for i in range(linhas):
        lista1 = lista1 + [min(matriz[i])]
    menor_tempo = min(lista1)
    for i in range(linhas):
        if list.count(matriz[i],menor_tempo) == 1:
            corredor = i+1
            volta = list.index(matriz[i],menor_tempo)+1
            return (corredor,menor_tempo,volta)