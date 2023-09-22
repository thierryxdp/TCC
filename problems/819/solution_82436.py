def filtraMultiplos(lista,n):
    'Retorna uma lista contendo os elementos que sao divisores de n'
    'lista, int -> lista'
    multiplos=[]
    for k in lista:
        if k%n==0:
            list.append(multiplos,k)
    return multiplos