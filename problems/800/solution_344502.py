def total(lista,valores):
    numero=0
    for produtos in lista:
        if produtos in valores:
            numero+=valores[produtos]
    return round(numero,2)