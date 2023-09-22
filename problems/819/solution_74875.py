def filtraMultiplos(lista,n):
    """coment"""
    multiplos=[]
    i=0
    while lista[i]%n!=0:
        multiplos=multiplos+[lista[i]]
        i=i+1
    return mutiplos