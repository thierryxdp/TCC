def maiores(lista, num):
    '''dada uma lista de numeros inteiros e um numero inteiro,
    e retornada uma nova lista com os numeros da lista antiga maiores
    que esse numero
    list, int -> list'''
    list.append(lista,num)
    list.sort(lista)
    a=list.index(lista,num)
    return lista[(a+1):]