def media_matriz(matriz):
    '''Função que recebe uma matriz de inteiros, nao vazia, e 
    retorna a media de todos os seus numeros.
    list(list) -> float'''
    
    med = 0
    
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
    
        resultado = med/(len(matriz)*len(matriz[0]))
    
    return round(resultado,2)