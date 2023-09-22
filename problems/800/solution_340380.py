def total(lista_compras, preco_produtos):
    '''Funcao que recebe uma lista de compras e uma tabela de
    precos de produtos disponiveis (em forma de dicionario) e retorna
    o valor total a ser gasto com os produtos da lista que estejam
    disponiveis.
    List, dict -> Float'''
    total = 0
    for produto in lista_compras:
        if produto in preco_produtos:
            total += preco_produtos.get(produto)
    return round(total,2)