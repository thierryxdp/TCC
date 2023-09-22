def filtraMultiplos (lista, n):
    """Receba uma lista e um numero n e retorna todos os multiplos de n nessa lista; lista, int -> lista"""
    multiplos = []
    proximo = 0
    for proximo in range(len(lista)):
        if lista[proximo]%n == 0:
            multiplos + [lista[proximo]]
    return multiplos