def conta_numero(numero, matriz):
    '''Função que retorna
    quantas vezes um inteiro aparece na matriz
    int,list -> int'''
    Qtnumero= 0
    
    for lin in range(len(matriz)):
        cuantidad= list.count(matriz[lin], numero)
        Qtnumero =  Qtnumero + cuantidad
        
    return Qtnumero