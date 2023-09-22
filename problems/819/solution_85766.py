def filtraMultiplos(lista,n):
    """Função que dada uma lista e um número n, retorna os números da lista multiplos de n. list -> list"""
    multiplosden = []
    for i in range(len(lista)):
        if lista[i]%n == 0:
            multiplosden.append(lista[i])
    return (multiplosden)