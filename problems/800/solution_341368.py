def total(lista,precos):
    """Função que retorna o valor total dos itens de uma lista disponíveis na loja"""
    """lista, dicionario -> float"""
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,precos[comprado])
           
    return round(sum(compras),2)