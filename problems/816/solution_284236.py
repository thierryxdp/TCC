def maiores(lista_numero,n):
    '''Dado uma lista de números e um número 'n', será retornado todos os números
    maiores que 'n' em ordem crescente.(lista,int=>lista)'''
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    x = list.index(lista_numero,n)
    lista_numero[0:x+1] = []

    return lista_numero