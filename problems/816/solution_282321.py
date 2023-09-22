def maiores(lista,n):
    '''Retorna uma lista em ordem crescente com os elementos
    maiores do que n; recebe como parâmetro uma lista e um
    número inteiro.List,Int-->List'''
    lista+=[n]
    list.sort(lista)
    pos_n=list.index(lista,n)
    return lista[:pos_n]