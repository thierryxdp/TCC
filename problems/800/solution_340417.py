def total(lista,precos):
    valor=0
    for item in lista:
        if item in precos:
            valor+=precos[item]
    return round(valor,2)