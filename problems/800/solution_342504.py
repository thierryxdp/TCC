def total(lista_compras,dicionario_preços):
soma=0
    for i in lista_compras:
        preço=dicionario_preços[i]
        soma=preço+soma
    return round(soma,2)