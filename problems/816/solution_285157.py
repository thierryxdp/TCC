def maiores(lista,n):
    '''função que retorna somente os numeros da lista maiores do que n;
    list,int->list'''
    list.sort(lista)
    a = list.index(lista,(n+1))
    return lista[a:]