def total(produto,dicionario):
    soma=0
    for comprar in dicionario:
        if str(produto) in dicionario:
            soma=soma+str(produto)
    return soma