def conta_numero(numero, matriz):
    '''Função que conta quantas vezes um número aparece na matriz;
       int, list => int'''
    
    resultado = 0
    
    for i in matriz:
        for e in i:
            resultado += 1
    return resultado