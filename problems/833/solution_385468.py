def conta_numero(numero,m):
    """dado um numero inteiro e uma matriz de inteiros de tamanho
    qualquer, conta e retorna quantas vezes aquele numero aparece
    na matriz
    int, list --> int"""
    x=0
    if len(m)==0:
        return 0
    else:
        numeroLinhas=len(m)
        numeroColunas=len(m[0])
        for i in range(len(m)):
            if numero in m[i]:
                x=x+m[i].count(numero)
        return x