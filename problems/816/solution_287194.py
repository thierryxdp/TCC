def maiores(lista_numero, n):
    '''funcao que retorna o numeros maiores que n contidos na lista_numero list,int->list'''
    if n in lista_numero:
    list.sort(lista_numero)
    lista1 = list.index(lista_numero,n)
    return lista_numero[lista1 + 1:]
else:
    list.append(lista_numero,n)
    list.sort(lista_numero)
    lista1 = list.index(lista_numero,n)
    return lista_numero[lista1 + 1:]