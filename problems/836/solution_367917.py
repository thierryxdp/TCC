def busca(matriz,string):
    lista = []
    posicao = 0
    contador = 0
    while posicao < len(matriz):
        if string in matriz[posicao]:
            list.append(lista,matriz[posicao])
        posicao = posicao + 1
    for elemento in len(lista[contador]):
        list.remove(lista,string)
        contador = contador + 1
    return lista