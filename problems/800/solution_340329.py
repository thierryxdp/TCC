def total (lista, dicio):
    valorTotal=0
    for el in lista:
        if el in dicio:
            valorTotal=valorTotal+dicio[el]
    return valorTotal