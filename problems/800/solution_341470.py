def total(compras,preco):
    """Funcao que recebe uma lista de compras e um dicionario contendo os precos dos produtos e retorna o valor total das compras.str,dict=>int"""
    valortotal=0
    for produto in compras:
        valortotal= valortotal + dict.get(preco,produto)
    return valortotal