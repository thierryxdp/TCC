def media_matriz(matriz):
    '''Retorna a média aaritmética dos elementos da matriz.
    list -> float'''
    elementos  = []
    contador = 0
    while contador < len(matriz):
        for i in range(len(matriz[contador])):
            list.append(elementos,matriz[contador][i])
        contador = contador + 1                
    return round (sum(elementos)/len(elementos),2)