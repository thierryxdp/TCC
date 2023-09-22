def filtraMultiplos(lista,n):
    """calculo e retorno de uma funcao que retorna multiplos de um numero de uma lista."""
    multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            multiplos=multiplos+[lista[i],]
        i=i+1
    return multiplos