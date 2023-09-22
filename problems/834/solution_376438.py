def media_matriz (matriz):
    '''Funcao que, dada uma matriz de inteiros não vazia, retorna a media de todos os numeros da matriz.
    list->float'''
    
    lista = [] 
    
    for linha in matriz:
        for i in linha:
            lista.append(i)
    return sum(lista)/len(lista)