def total(produto,dicionario):
    soma=0
    comprar=0
    for comprar in range(0,len(dicionario)):
        if produto[comprar] in dicionario.keys():
            soma=dicionario[produto[comprar]]+soma
    return round(soma,2)