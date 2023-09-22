def filtra_pares(tupla):
    '''Dada um tupla de quatro elementos inteiros,
    retorna a mesma contendo somente os elementos 
    pares da tupla.
    tuple --> tuple''' 
    F=()
    w,x,y,z = tupla
    if w%2==0:
        F=F+[w,]
    if x%2==0:
        F=F+[x,]
    if y%2==0:
        F=F+[y,]
    if z%2==0:
        F=F+[z,]
        return F