def filtraMultiplos(ln,n):
    """
    Retorna uma lista com os múltiplos de n, dada uma lista original.
    list, int -> list
    """
    lmultiplos=[]
    i=0
    while i<len(ln):
        if ln[i]%n==0:
            lmultiplos= lmultiplos+[ln[i]]
        i=i+1
    return lmultiplos