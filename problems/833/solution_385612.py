def conta_numero(numero,matriz):
    '''
    	essa função recebe uma matriz e conta a quantidades de vezes que um determinado 
        numero aparece na mesma.
        num, list -> num
    '''
    if numero not in matriz:
        return 0
    else:
        return list.count(len(matriz[0]), numero)