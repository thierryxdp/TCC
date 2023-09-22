def total(prod,pr):
    """ funcao que recebe como entrada uma lista de produtos
    "prod", e um dicionário "pr" contendo os preços, e retorna
    o valor total dos itens da lista que estejam disponíveis"""
    """ list, dict -> float """
    valor=0
    for produto in prod:
        valor= valor + pr[produto]
    return round(valor,2)
#Casos de teste:
""" total(["chocolate","farinha","leite"], {"chocolate":10.00,"farinha":2.00,"leite":3.50})
>>> 15.5 """