def conta_numero(numero,matriz):
    '''
    	essa função recebe uma matriz e conta a quantidades de vezes que um determinado 
        numero aparece na mesma.
        num, list -> num
    '''
    for elem in matriz:
        qtd_elem = 0
        if elem == numero:
            qtd_elem = qtd_elem +1
    return qtd_elem