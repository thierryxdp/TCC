def total (lista,precos):
    total=0
    for produtos in lista:
        if produtos in precos:
          valores=precos[produtos]
        total+=valores
    return total