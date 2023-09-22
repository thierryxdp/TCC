def media_matriz(matriz):
    ''' funcao que dado uma matriz nao vazia retorna a media de todos os seus numeros
    list->float'''
    lista = []
    for linha in matriz:
        for i in linha:
            lista.append(i)
    return round(sum(lista)/len(lista),2)