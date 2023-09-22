def filtraMultiplos(l1,n):
    '''
    Função que ao receber uma lista de numeros(n) retorna outra lista contendo todos os elementos da lista originalo
    divisiveis por n
    list -> list
    '''
    l2=0
    i=0
    while i<len(l1):
        if l1[i]/n:
            l2=list(l1[i])
        i = i+1
    return l2