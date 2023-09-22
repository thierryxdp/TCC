def melhor_volta (matriz):
    '''Retorna o campeão, o melhor tempo e em que volta de uma corrida de Kart.
    list -> str, float, int'''
    elementos  = []
    contador = 0
    contador1 = 0
    while contador < len(matriz):
        for i in range(len(matriz[contador])):
            list.append(elementos,matriz[contador][i])
        contador = contador + 1
    tempo = min (elementos)
    while contador1 < len(matriz):
        if tempo in matriz[contador1]:
            campeao = contador1
            volta = list.index(matriz[contador1],tempo)
        contador1 = contador1 + 1
    return campeao, tempo, volta + 1