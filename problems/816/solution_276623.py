def maiores(x,y):
    '''Função que dada uma lista retorna todos os números maiores que n
       list,int->list'''
    x.insert(0,y)
    x.sort()
    a=x.index(y)
    return x[a+1:]