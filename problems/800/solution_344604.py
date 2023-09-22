def total(lista, produtos):
    '''A função calcula o valor total das
    compras a depender dos preços e da dis-
    ponibilidade dos produtos.
    list, dict --> float'''

    total = 0
    counter = 0
    limit = len(lista)

    while counter < limit:
        total += produtos[lista[counter]]
        counter += 1

    return round(total, 2)