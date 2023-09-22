def total(lista=[],dicio={}):
    """funcao que recebe uma lista de compras e um dicionario com os precos e retorna o valor total dos itens da lista que estao disponiveis na loja. list, dict -> float"""
    cont=0.0
    for i in lista:
        cont+=dicio[i]
    return round(cont,2)