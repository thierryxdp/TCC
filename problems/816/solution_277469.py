def maiores(lista, n):
    '''função que dada uma lista de numeros inteiros e um numero inteiro n retorna outa lista; list,int->list'''
    n = 1
    lista_final = []
    for elemento in lista:
        if elemento > n:
            list.sort(lista)
            list.count(lista, n)
            lista_final.append(elemento)
            lista_final.sort(elemento)
            return[i for i in lista if i > n ]