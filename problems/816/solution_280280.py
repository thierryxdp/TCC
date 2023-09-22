def maiores(num_inteiros,n):
    '''dada uma lista, e um n, retorna uma lista
    com valores maiores do que n; lista,int->lista'''
    list.append(num_inteiros,n)
    list.sort(num_inteiros)
    ps=list.index(num_inteiros,n)
    lista=num_inteiros[ps+1:]
    return lista