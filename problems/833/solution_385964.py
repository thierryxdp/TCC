def conta_numero(numero,matriz):
    ''''''
    contagem=0
    for lista in matriz:
        contagem+=list.count(lista,numero)
    return contagem