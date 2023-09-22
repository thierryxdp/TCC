def busca(matriz,string):
    lista = []
    posicao = 0
    string = string
    while posicao < len(matriz):
        if string in matriz[posicao]:
            list.append(lista,matriz[posicao])
        posicao = posicao + 1
    return lista