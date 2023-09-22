def soma_h(n):
    lista = list(range(1,n+1))
    i = 0
    div= 0
    for x in lista:
        y = 1/x
        div = div + (y)
    return round(div, 2 )