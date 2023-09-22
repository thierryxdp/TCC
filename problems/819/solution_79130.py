def filtraMultiplos(lista, multiplo):
    nova = []
    contador = 0
    quantidade = len(lista)
    while contador < quantidade:
        if lista[contador] % multiplo == 0:
            nova = nova + [lista[contador]]
        contador = contador + 1
    return nova