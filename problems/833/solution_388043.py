def conta_numero(numero,matriz):
    contador = 0
    for quantidade in matriz:
        qtd = list.count(quantidade,numero)
        contador = contador + qtd
    return contador