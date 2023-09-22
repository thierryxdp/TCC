def media_matriz(matriz):
    '''Função que dada uma matriz retorna a média
    dos elementos dessa matriz
    list[int]->float'''
    
    soma=0
    qtd_elementos=0
    
    for linha in matriz:
        for elemento in linha:
            soma=soma+elemento
            qtd_elementos+=1
    
    media=soma/qtd_elementos
            
    return round(media,2)