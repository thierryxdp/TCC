def maiores(num_inteiros,n):
    '''dada uma lista, e um n pertencente à ela, retorna uma lista
    com valores maiores do que n; lista,int->lista'''
    list.sort(num_inteiros)
    ps=list.index(num_inteiros,n)
    lista=num_inteiros[ps+1:]
    return lista