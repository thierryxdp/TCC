def filtraMultiplos(lista,n):
    """Recebe uma lista e um número inteiro n e retorna uma nova lista r contendo todos os números inteiros da lista fornecida que são divisíveis por n"""
    r=[]
    x=int
    for x in lista:
        if x%n!=0:
            r==r
        else:
            r==r.append(x)
    return r