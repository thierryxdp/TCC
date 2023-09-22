def total(lista,precos):
    valor_t = 0
    for p in lista:
        if p in precos:
            valor_t = valor_t + precos[p]
    return round(valor_t,2)