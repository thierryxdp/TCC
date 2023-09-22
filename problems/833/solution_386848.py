def conta_numero(numero,matriz):
    '''
    função que dado um número inteiro e uma matriz de inteiros
    de qualquer tamanho, conta e retorna quantas vezes o numero
    aparece na matriz.
    '''
    linha = 0
    for item in matriz[linha]:
        for item2 in matriz[linha][contar]:
            if numero == matriz[linha][contar]:
                vezes += 1
                contar += 1
    linha += 1  
    return vezes