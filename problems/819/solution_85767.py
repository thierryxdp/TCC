def filtraMultiplos(lista,n):
    """Função que dada uma lista e um número n, retorna os números da lista multiplos de n. list -> list"""
    multiplosden = []
    for k in range(len(lista)):
        if lista[k]%n == 0:
            multiplosden.append(lista[k])
    return (multiplosden)