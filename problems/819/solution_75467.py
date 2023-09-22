def filtraMultiplos (lista, n):
    """Receba uma lista e um numero n e retorna todos os multiplos de n nessa lista; lista, int -> lista"""
    return [n for n in lista if n % lista]