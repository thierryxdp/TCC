def acima_da(lista,n):
    '''Recebe uma lista de números e um número n, e retorna outra lista com todos os números maiores que n.
list, int -> list'''
    x = (sum(lista))/(len(lista))
    maiores_que = [numero for numero in lista if numero > x]
    list.sort(maiores_que)
    return maiores_que