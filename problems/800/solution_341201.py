def total(lista_compras,preco_loja):
        '''retorna o preço da lista de
        compras list, dict --> float'''
        preco_compras=0
        for item in lista_compras:
            preco_compras+=dict.get(preco_loja