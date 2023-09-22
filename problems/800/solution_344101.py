def total(compras, precos):
    total = 0
    for item in compras:
        total = total + precos[item]
    return round(total, 2)