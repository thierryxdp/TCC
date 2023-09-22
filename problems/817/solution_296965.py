def maiores(lista,n):
    '''função que retorna uma lista que contem todos os numeros dada uma lista 
    original maiores que n, ordenados em ordem crescente. 
    list,int->list'''
    x = ([i for i in lista if i > n])
    return sorted(x)
def acima_da_media(listatodos):
    '''função que retorna uma lista com as notas acima da média, dada a lista das notas de todos
    list --> list'''
    a = sum(lista)
    b = len(lista)
    c = a/b
    return maiores(listatodos,c)