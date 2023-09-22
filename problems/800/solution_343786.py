def total(lista,dic):
    """Recebe uma lista contendo produtos e um dicionário
    com o valor dos produtos e calcula o valor final da compra.
    Assinatura: list, dict -> float"""
    total=0
    for palavra in lista:
        if palavra in dic:
            total+=dic[palavra]
    return round(total,2)