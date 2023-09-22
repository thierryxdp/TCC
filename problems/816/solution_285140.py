def maiores(lista,n):
    '''função que retorna somente os numeros da lista maiores do que n;
    list,int->list'''
    ordem = list.sort(lista)
    return ordem[n:]