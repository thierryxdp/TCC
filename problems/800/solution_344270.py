def total(compras,precos):
    soma=0
    for produto in compras:
        if produto in precos:
            soma+=float(precos[produto])
    return round(soma,2)