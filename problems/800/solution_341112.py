def total(compras,precos):
    """retorna o custo de uma lista de compras;
    list[str],dict{str:float}->float"""
    custo=0
    for produto in compras:
        custo+=precos[produto]
    return round(custo,2)