def acima_da_media(listatodos):
    '''função que retorna uma lista com as notas acima da média, dada a lista das notas de todos
    list --> list'''
    a = sum(listatodos)
    b = len(listatodos)
    c = a/b
    return maiores(listatodos,c)