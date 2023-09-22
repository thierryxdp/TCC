def total(lista_de_compras,produtos):
    """funcao que ao receber uma lista com as strings de produtos e um dicionario contendo os precos, retorna o gasto total necessario para adquirir a mercadoria;
    list de str, dict -> float"""
    gasto_total=0
    for item_procurado in produtos:
        gasto_total=gasto_total+produtos[item_procurado]
    return gasto_total