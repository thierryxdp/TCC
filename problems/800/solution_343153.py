def total(produto,dicionario):
    soma=0
    for comprar in range(0,len(dicionario)):
        if produto in dicionario:
            soma=dict.values(produto)
    return soma