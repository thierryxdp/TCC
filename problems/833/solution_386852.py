def conta_numero(numero,matriz):
    '''
    função que dado um número inteiro e uma matriz de inteiros
    de qualquer tamanho, conta e retorna quantas vezes o numero
    aparece na matriz.
    '''
    vezes = 0
    linha = 0
    for item in matriz:
        contar = 0
        for item2 in matriz[linha]:
            if numero == item2:
                vezes += 1
                contar += 1
    linha += 1  
    return vezes