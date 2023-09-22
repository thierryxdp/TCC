def total(lista,dicionario):
    soma=0
    for comprar in dicionario:
        if lista in dicionario:
            soma=soma+comprar
    return soma