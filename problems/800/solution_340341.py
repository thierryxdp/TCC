def total(lista_compras,mercado):
    '''função que retorna o preço total da soma dos produtos
    que estão na lista, dado o preço dos produtos em um dicionario
    list,dict->float'''
    soma=0
    for produtos in mercado:
        preco=mercado[produtos]
        soma=soma+preco
    return soma