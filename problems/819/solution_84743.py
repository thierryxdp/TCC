def filtraMultiplos (ln,n):
    '''função em que dada uma lista de números (ln) e um número (n) retorne
    retorne uma lista com todos os elementos da lista original que são
    divisíveis por esse número;
    list, int -> list'''
    i=0
    multiplos=[]
    while i<len(ln):
        if ln[i]%n==0:
            list.append(multiplos,ln[i])
        i=i+1
    return multiplos