def conta_numero(numero,matriz):
    '''Funcao que retorna quantas vezes o numero de entrada aparece na
    matriz de entrada.
    int,list->int'''
    x=0
    total=0
    k=range(len(matriz))
    while x in k:
        if numero in matriz[x]:
            y=list.count(matriz[x],numero)
            total=total+y
        x=x+1
    return total