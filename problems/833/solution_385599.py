def conta_numero(numero,matriz):
    '''
    	essa função recebe uma matriz e conta a quantidades de vezes que um determinado 
        numero aparece na mesma.
        num, list -> num
    '''
    i = 0
    x = 0
    while i < len(matriz):
        if numero in matriz:
            x = x+1
        i = i+1    
    return x