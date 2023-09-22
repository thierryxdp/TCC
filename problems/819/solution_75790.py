def filtraMultiplos(l,n):
    """recebe uma lista de números "l" e um número "n" e retorna outra lista cujos elementos são os elementos da lista original que são divisíveis por n;list,int->list"""
    multiplos=[]
    i=0
    while i<len(l):
        if l[i]%n==0:
            multiplos=multiplos+[l[i]]
        i=i+1
    return multiplos