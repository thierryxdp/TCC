def filtra_pares (tupla):
    """Retorna uma tupla apenas com os números pares dados como entrada,
    mantendo sua ordem: tuple->tuple"""
    return ([ n for n in tupla if n % 2 == 0 ])