def media_matriz(matriz):
    '''teste'''
    
    soma=0
    qtd_elementos=0
    
    for linha in matriz:
        for elemento in linha:
            soma=soma+elemento
            qtd_elementos+=1
    
    media=soma/qtd_elementos
            
    return round(media,2)