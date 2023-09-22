def conta_numero(n,matriz):
    """funcao que dado um numero (n) inteiro e uma matriz de inteiros de qualquer
    tamanho, e conta quantas vezes aquele numero apareceu na matriz. int,list->int"""
    ocorrencia=[]
    for J in matriz :
        for i in J:
            if i==n:
                list.append(ocorrencia,1)
    return sum(ocorrencia)