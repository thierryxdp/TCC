def maiores(lista,n):
    '''Dado uma lista de numeros, retorne outra lista com números maiores que n; list,int -> list'''
    if n in lista:
        list.sort(lista)
        ocorrencia=list.index(lista,n)
        b=lista[ocorrencia+1:]
        return b
    list.append(lista,n)
    list.sort(lista)
    ocorrencia=list.index(lista,n)
    a=lista[ocorrencia+1:]
    return a