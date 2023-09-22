def conta_numero(numero,matriz):
    '''
    Função que retorna a quantidade de vezes que um número aparece em uma matriz.
    int,list -> int
    '''
    qtd_numero = 0
    for repeticao in numero:
            if repeticao == numero:
                qtd_numero = qtd_numero + 1
    return qtd_numero