def conta_numero(num,matriz):
    """função que dado um número e uma matriz, retorna a 
    quantidade de vezes que esse número apareceu na matriz
    int,list=>int"""
    contador=0
    for i in matriz:
        for j in i:
            if num==j:
                contador=contador+1
    return contador