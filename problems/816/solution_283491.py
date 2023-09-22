def maiores(lista,n):
    '''Insere o parâmetro n no parâmetro lista e
    e coloca em ordem crescente e retorna apenas maiores que
    o valor de n
    list,int->list'''
    l=list.append(lista,n)
    l1=list.sort(lista)
    l2=list.index(lista,n)
    l3=lista[l2+1:]
    return l3