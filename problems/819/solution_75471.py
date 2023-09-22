def filtraMultiplos (lista, n):
    """Receba uma lista e um numero n e retorna todos os multiplos de n nessa lista; lista, int -> lista"""
    listaf = ()
    proximo = 0
    if lista[proximo]%n == 0:
        listaf = listaf + (lista[proximo])
        return listaf