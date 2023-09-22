def total (lista, dicio):
    valorTotal=0
    for produto in lista:
        if produto in dicio:
            valorTotal=valorTotal+dicio[produto]
    return valorTotal