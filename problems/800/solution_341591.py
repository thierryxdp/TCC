def total(lista,dic):
    """retorna o valor total dos itens"""
    valor = 0
    for item in lista:
        if item in dic:
            valor = valor + dict.get(dic,item)
    return round(valor,2)