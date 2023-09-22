def maiores(lista,n):
    '''função que retorna uma lista que contem todos os numeros dada uma lista 
    original maiores que n, ordenados em ordem crescente. 
    list,int->list'''
    x = ([i for i in lista if i > n])
    return sorted(x)