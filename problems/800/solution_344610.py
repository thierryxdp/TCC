def total(lista=[],dict=[]):
    cont = 0
    n = len(lista)
    x = 0
    while x < n+1:
        cont += dict[x]
        x += 1
    return(round(cont,2))