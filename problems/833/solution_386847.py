def conta_numero(numero,matriz):
    '''
    função que dado um número inteiro e uma matriz de inteiros
    de qualquer tamanho, conta e retorna quantas vezes o numero
    aparece na matriz.
    '''
    
    
    
    for item in matriz:
        vezes = 0
        linha = 0
        contar = 0
        if numero == matriz[linha][contar]:
            vezes += 1
            contar += 1
        linha += 1  
    return vezes