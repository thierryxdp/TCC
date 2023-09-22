def conta_numero(numero,matriz):
    '''
    Função que retorna a quantidade de vezes que um número aparece em uma matriz.
    int,list -> int
    '''
    qtd_elem = 0
    for elem in matriz:
            if elem == numero:
                qtd_elem = qtd_elem + 1
    return qtd_elem