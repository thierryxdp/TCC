def total (lista,dicionario):
    """retorna o valor total dos itens da lista que estejam disponíveis nesta loja"""
    valor_total=0
    for ELEMENTO in lista:
        valor_total= dicionario[ELEMENTO]
    return valor_total