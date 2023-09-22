def conta_numero(numero,matriz):
    '''Função que conta e retorna quantas vezes aquele 
    número aparece na matriz.
    numero=int,matriz=list->int'''
    p=0
    tt=0
    w=range(len(matriz))
    while p in w:
        if numero in matriz[p]:
            t=list.count(matriz[p],numero)
            tt=tt+t
        p=p+1
    return tt