def filtraMultiplos(lista,n):
    """coment"""
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[i]%n==0:
            multiplos=multiplos+[lista[i]]
        proximo=proximo+1
    return multiplos