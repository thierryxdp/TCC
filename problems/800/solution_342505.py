def total(lista_compras,dicionario_precos):
soma=0
    for i in lista_compras:
        preco=dicionario_precos[i]
        soma=preco+soma
    return round(soma,2)