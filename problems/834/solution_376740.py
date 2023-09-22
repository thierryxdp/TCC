def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia retorna a média de todos os números
       desta matriz com duas casas decimais de precisão.
       list -> floot"""
    
    somaNumerador = 0
    somaDenominador = 0
    
    for indice in range(len(matriz)):
        pivo = matriz[indice]
        
        for i in range(len(pivo)):
            somaNumerador += sum(pivo)
            somaDenominador += len(pivo)
            
    return somaNumerador / somaDenominador