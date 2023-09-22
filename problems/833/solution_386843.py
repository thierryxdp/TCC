def conta_numero(numero,matriz):
    '''
    função que dado um número inteiro e uma matriz de inteiros
    de qualquer tamanho, conta e retorna quantas vezes o numero
    aparece na matriz.
    '''
    
    vezes = 0
    
    for item in matriz:
        linha = 0
        contar = 0
        if numero == matriz[elemento][contar]:
            vezes += 1
            contar += 1
    elemento += 1  
    return vezes