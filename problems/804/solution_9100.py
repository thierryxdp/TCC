def filtra_pares(tupla):
    """A função retorna somente os números pares da tupla;
	tuple -> tuple"""
    pares = (n for n in tupla if n%2 == 0)
    return pares