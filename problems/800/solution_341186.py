def total(lista,dicio):
    ''' recebe uma lista de compras e um dicionario contendo os produtos e os preços desses
    em uma determinada loja. Retorna a soma desses produtos.
    list , dict --> float'''
    
    soma = 0
    for produto in lista:
        if produto in dicio:
            soma = soma + dicio.get(produto)
    return round(soma,2)