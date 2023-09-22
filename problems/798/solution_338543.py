def total(lista,dicionario):
    """Função que retorna o valor total dos itens de compra disponíveis
na loja ; list,dict -> float"""
    valor=0
    for produto in lista:
        if produto in dicionario:
            valor+=dicionario[produto]
    return round(valor,2)