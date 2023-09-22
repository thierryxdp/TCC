def conta_numero(numero,matriz):
    '''
    	essa função recebe uma matriz e conta a quantidades de vezes que um determinado 
        numero aparece na mesma.
        num, list -> num
    '''
    x = 0
    for elem in matriz:
        if elem == numero:
            x = x+1
    return x