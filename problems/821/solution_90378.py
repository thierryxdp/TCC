def fatorial(n):
    """
    recebe um número e retorna o fatorial do mesmo
    """
    x=n
    tupla=()
    while x>0:
        tupla=tupla+(x,)
        x=x-1
    i=0
    y=1
    while i<len(tupla):
        y=y*tupla[i]
        i=i+1
    return y