def maiores(lista,n):
    '''A partir de uma lista de numeros inteiros e um numero n
    retorna outra lista com todos os numeros maiores que
    n(inteiro) presentes na lista
    list,int -> list'''
    list.append(lista,n)
    list.sort(lista)
    list.reverse(lista)
    posicaon = list.index(lista,n)
    list.reverse(lista[:posicaon])
    return lista