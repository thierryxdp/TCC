def total(produto,dicionario):
    soma=0
    for comprar in dicionario:
        if produto in dicionario:
            soma=dict.values(produto)
    return soma