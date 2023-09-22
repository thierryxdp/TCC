def qtd_divisores(x):
    divs = 0
    cont=x
    while cont>0:
        if x % cont == 0:
            divs++
    return divs