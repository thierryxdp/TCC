def filtraMultiplos(lista,n):
    """essa funçao recebe uma lista e um numero que retorna os multiplos do numero dentro da lista""" 
    multiplos=[]
    x=0
    while x <len(lista):
        if lista[x]%n==0:
            multiplos=multiplos+[lista[x],]
        x=x+1
    return multiplos