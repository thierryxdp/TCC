def filtraMultiplos(lista_numeros, n):
    nova_lista = []
    contador = 0
    while contador < len(lista_numeros):
        if lista_numeros[contador] % n == 0:
            nova_lista = nova_lista + lista_numeros[contador]
        contador = contador + 1
    return nova_lista