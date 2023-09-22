def total(a, b):
    preco = 0
    for x in a:
        preco += b(x)
    return round(preco, 2)