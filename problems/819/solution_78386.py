def filtraMultiplos(l,n):
    """dada uma lista de numeros e um numero n, filtra os elementos da lista que sao divisiveis por n
    l->lista
    n->numero qualquer
    list,int->list"""
    multiplos=[]
    proximo=0
    while proximo<len(l):
        if l(proximo)%n==0:
            multiplos=multiplos+[l(proximo),]
        proximo=proximo+1
    return multiplos