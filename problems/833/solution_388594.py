def conta_numero(numero,matriz):
    m=0
    for x in matriz:
        m= m + list.count(x,numero)
    return m