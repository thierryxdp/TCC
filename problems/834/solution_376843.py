def media_matriz(matriz):
    '''recebe uma matriz e retorna a média de todos os números da matriz.
    list(list) -> float'''
    lista = []
    qtd_elementos = len(matriz)*len(matriz[0])
    for linha in matriz:
        pos = 0
        soma_elementos = sum(linha)
        list.append(lista,soma_elementos)
        pos = pos + 1
    return round(sum(lista)/qtd_elementos,2)