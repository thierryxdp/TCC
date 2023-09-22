# 
def total(lista,produtos):
    valor_total=0
    for i in range(len(lista)):
        if lista[i] in produtos:
            valor=produtos.get(lista[i])
        valor_total+=valor
    return float(valor_total)