def qtd_divisores(x):
    divs = 0
    for num in x:
        if x%num==0:
            divs++
    return divs