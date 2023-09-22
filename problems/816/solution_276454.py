def maiores(lista,numero):
    '''retorna somente os números maiores que n; (list;int->'''

    lista2=[numero]
    lista3=lista+lista2
    
    list.sort(lista3)
    n=list.index(lista3,numero)
    y=list.count(lista3,numero)
    lista4=lista[n+y-1:]

    return lista4