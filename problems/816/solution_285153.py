def maiores(lista,n):
    '''função que retorna somente os numeros da lista maiores do que n;
    list,int->list'''
    a = list.count(lista,n)
    list.sort(lista)
    if n in lista:
        return lista > n