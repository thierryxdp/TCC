def busca(string,matriz):
    lista = []
    posicao = 0
    contador = 0
    while posicao < len(matriz):
        if string in matriz[posicao]:
            list.remove(matriz[posicao],string)
            list.append(lista,matriz[posicao])
        posicao = posicao + 1   
    return lista