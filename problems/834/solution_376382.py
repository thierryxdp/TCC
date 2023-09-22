def media_matriz(m):
    '''Dada uma matriz de números inteiros não vazia, retorna a média
    de todos os números da matriz.
    list --> int'''
    media = 0
    
    for linha in m:
        for elemento in linha:
            media = media + elemento 
        
        resultado = media/(len(m)*len(m[0]))
        
    return round(resultado,2)