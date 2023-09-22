def conta_numero(numero,m):
    '''Retorna quantas vezes o numero aparece na matriz dado um numeor inteiro e uma matriz de inteiros'''
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