def filtraMultiplos(l,n):
    """ Dada um lista com numeros inteiros e um numero n , vamos retornar uma nova lista
        com os multiplos de n.
        Entrada ---> List
        Saida   ---> List """
    
    x=0
    while x<len(l):
        if l[x]%n!=0:
            l.pop(x)
        else:
            x=x+1
    return l


""" Teste:
    Resultados Esperados:
    [1,2,3,4,5,6,7,8,9] ----> [2,4,6,8]
    [1,2,3,4,5,6,7,8,9] ----> [3,6,9]
    Resultados Obitidos:
    >>> filtraMultiplos([1,2,3,4,5,6,7,8,9],2)
    [2, 4, 6, 8]
    >>> filtraMultiplos([1,2,3,4,5,6,7,8,9],3)
    [3, 6, 9]    """