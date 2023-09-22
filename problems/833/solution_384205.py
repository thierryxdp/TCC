def conta_numero(numero,matriz):
    '''funcao que conta e retorna o numero de vezes que o 
    um determinado numero aparece na matriz; int->list'''
    f=0
    soma=0
    g=range(len(matriz))
    while f in g:
        if numero in matriz[f]:
            i= list.count(matriz[f], numero)
            soma=soma+i
        f=f+1
    return soma