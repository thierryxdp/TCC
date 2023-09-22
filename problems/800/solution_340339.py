def total(lista_compras,mercado):
    '''função que retorna o preço total da soma dos produtos
    que estão na lista, dado o preço dos produtos em um dicionario
    list,dict->float'''
    soma=0
    for lista_compras in mercado:
        preco=mercado[lista_compras]
        soma=soma+preco
    return soma