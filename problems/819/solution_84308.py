def filtraMultiplos(l,n):
    """Funçao que denomina os elementos da lista e divide com n, caso de resto 0 ele retorna esse
    valor para dentro de outra lista: d"""
    d=[]
    for numeros in l:
        if (numeros % n) == 0:
            d= d + [numeros,]
    return d