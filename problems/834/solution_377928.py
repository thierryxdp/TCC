def media_matriz(m):
    """função que retorna a media de todos o números da matriz, através de uma matriz de entrada não vazia;
    Entrada: list
    Saída: int"""
    resultado = 0
    elementos = 0
    
    for indice in range(len(m)):
        x = sum(m[indice])
        y = len(m[indice])
        resultado = resultado + x
        elementos = elementos + y
    return round(resultado / elementos)