def total(lista_compras,produtos_loja):
    '''calcula e retorna o preco total das
    compras 
    list,dict --> float'''
    preco_compras=0
    for item in lista_compras:
        preco_compras+=dict.get(produtos_loja,item)
    return round(preco_compras,2)