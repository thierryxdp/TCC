def filtraMultiplos(lista,n):
    """Função que dada uma lista e um número n, retorna os números da lista multiplos de n. list -> list"""
    multiplosden = []
    for m in range(len(lista)):
        if lista[m]%n == 0:
            multiplosden.append(lista[m])
    return (multiplosden)