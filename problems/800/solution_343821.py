def total (ls,dicio):
    preco = 0
    for e in ls:
        d = dicio[e]
        preco = preco + d
    return round (preco,2)