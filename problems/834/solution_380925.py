def media_matriz(matriz):
    '''Função que retorna a média de todos os números da matriz;
    list->float'''
    lista = [] 
    for linha in matriz:
        for i in linha:
            lista.append(i)
    return round(sum(lista)/len(lista),2)