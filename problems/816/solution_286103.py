def maiores(inteiros,n):
    '''funcao lista de numeros inteiros e um numero n, retorna outra lista em ordem crescente de numeros maiores que n
    list->list'''
    list.append(inteiros,n)
    list.sort(inteiros)
    a=inteiros.index(n)
    novos_inteiros=inteiros[a:]
    list.remove(novos_inteiros,n)
    return inteiros