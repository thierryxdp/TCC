def filtraMultiplos(x,n):
    """Função que filtra de uma lista, somente os números múltiplos de n"""
    """int-->int"""
    lista=[]
    i=0
    while i<len(x):
        if x[i]%n==0:
            lista.append(x[i])
        i+=1
    return lista