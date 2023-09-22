def conta_numero(n,matriz):
    """funcao que dado um numero (n) inteiro e uma matriz de inteiros de qualquer
    tamanho, e conta quantas vezes aquele numero apareceu na matriz. int,list->int"""
    ocorrencia=0
    for nlinhas in matriz :
        for i in nlinhas:
            if i==n:
                ocorrencia +=1
    return ocorrencia