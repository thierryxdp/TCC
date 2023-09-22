def total(compras,precos):
    pagar=0
    for i in compras:
        if i in precos:
            pagar=pagar+precos[i]
    return round(pagar,2)