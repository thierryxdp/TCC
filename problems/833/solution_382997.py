def conta_numero(numero, matriz):
    ''' Retorna quantas vezes um dado número aparece
    numa dada matriz;
    int, list -> int'''
    
    contador = 0
    
    for linha in matriz:
        contador += linha.count(numero)
    
    return contador