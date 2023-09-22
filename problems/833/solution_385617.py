def conta_numero(numero,matriz):
    '''
    	essa função recebe uma matriz e conta a quantidades de vezes que um determinado 
        numero aparece na mesma.
        num, list -> num
    '''
    qtd = []
    for elem in range(len(matriz)):
        for x in elem:
            if x == numero:
                qtd_2 = qtd_2 + 1
        list.append(qtd, qtd_2)
    return qtd