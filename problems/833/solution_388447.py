def conta_numero(numero,m):
    '''     Dado uma matriz de números inteiros
     é retornado quantas vezes um determinado
     número aparece na matriz.
     assinatura: int,lista(no caso matriz) ---> int '''
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