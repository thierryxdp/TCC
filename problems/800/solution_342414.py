def total(lista,dicionario):
    """dada uma lista de compras de entrada e um dicionário
    contendo os produtos como chave e seus preços como valor
    retorna o preço total da lista de compras"""
    valor=0
    for i in lista:
        if i in dicionario:
            valor=valor+dicionario[i]
    return round(valor,2)