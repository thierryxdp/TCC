def filtraMultiplos(lista,numero):
    """funcao que recebe uma lista com numeros e um numero n e retorna uma lista com os os numeors que forem divisiveis por n.
    lista,int->lista"""
    i=0
    x=[]
    while i<len(lista):
        if lista[i]%numero==0:
            list.append(x,lista[i])
        i=i+1
    return x