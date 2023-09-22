def total(lista,produtos):
    "Calcula o valor da compra da lista dos produtos comprados; lista, dici-> float"
    r=0
    for i in lista:
        if i in produtos:
            r+=produtos[i]
    return round(r,2)