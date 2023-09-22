def soma_h(n):
    """Essa função serve para calcular e retornar o valor H com N termos
    int->float"""
    h = 0
    den = 0
    for i in range(n):
        num = 1
        den = den + 1
        h += (num/den)
    return round(h,2)

#soma_h(2) == 1.5
#soma_h(7) == 2.59
#soma_h(100) == 5.19