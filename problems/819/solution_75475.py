def filtraMultiplos (lista, n):
    """Receba uma lista e um numero n e retorna todos os multiplos de n nessa lista; lista, int -> lista"""
    listaf = ()
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]/n== 0:
            listaf = listaf + (lsta[proximo],)
            proximo = proximo + 1
            return listaf