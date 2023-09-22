def soma_h(n):
    #int > int
    h = []
    index = 1
    while index <= n:
        if index <= n:
            h = h + [(1/index)]
        index = index + 1
    for x in h:
        somaH = sum(h)
    return round(somaH, 2)