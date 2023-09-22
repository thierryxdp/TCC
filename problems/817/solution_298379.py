def maiores(lista,n):
    '''Retorna uma lista que contem todos os numeros inteiros maiores que n, dados uma lista de numeros inteiros e um numero inteiro list,int->list'''
    x = ([i for i in lista if i > n])
    return sorted(x)
def acima_da_media(listatodos):
    '''função que retorna uma lista com as notas acima da média, dada a lista das notas de todos
    list --> list'''
    a = sum(listatodos)
    b = len(listatodos)
    c = a/b
    return maiores(listatodos,c)