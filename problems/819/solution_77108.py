def filtraMultiplos (lista, n):
    """Receba uma lista e um numero n e retorna todos os multiplos de n nessa lista; lista, int -> lista"""
    multiplos = ()
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            multiplos + (lista[proximo])
            proximo = proximo + 1
    return multiplos