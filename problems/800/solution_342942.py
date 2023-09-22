def total(produto,dicionario):
    soma=0
    for comprar in dicionario:
        if str produto in dicionario:
            soma=soma+comprar
    return soma