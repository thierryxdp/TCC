def conta_numero(numero,matriz):
    contador = 0
    for linha in matriz:
        contador = contador + list.count(linha,numero)
    return contador