def total(l,d):
    """Função que, dada uma lista de compras e um dicionário com
    os valores associados, retorna o total da compra
    list, dict --> float"""
    tot=0
    for elementos in l:
        tot+=d[elementos]
    return round(tot,2)