def conta_numero(numero,matriz):
    '''
    função que dado um numero inteiro e uma matriz (somente com numeros inteiros),
    conta e retorna quantas vezes o numero aparece na matriz 
    int,list->int
    '''
    repeticao=0
    for n in range(len(matriz)):
        
        M=matriz[n]
        for k in range(len(M)):
            if M[k]==numero:
                repeticao=repeticao+1
            else:
                repeticao
    return repeticao