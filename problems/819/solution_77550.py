def filtraMultiplos(lista,n):
    """funcao que retorna uma lista com todos os multiplos de n em uma determinada lista; list, int->list"""
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n==0:
            multiplos=multiplos+[lista[i]]
        i=i+1
    return multiplos