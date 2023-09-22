def total(lista,produtos):
    ''' Esta função faz a soma dos produtos de uma determinada lista,
    retornando o total daos produtos;list,dici->float'''
    conta=0
    for item in lista:
        valor=dict.get(produtos,item)
        conta+=valor
    return round(conta,2)