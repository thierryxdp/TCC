def total(lista, produtos):
    '''A função calcula o valor total das
    compras a depender dos preços e da dis-
    ponibilidade dos produtos.
    list, dict --> float'''
    
    counter = 0
    total = 0
    
    for elementos in lista:
        if lista[counter] in produtos:
            total += produtos[lista[counter]]
            counter += 1
    return round(total, 2)