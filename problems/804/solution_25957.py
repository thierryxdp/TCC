def filtra_pares(t):
    """função que retorna somente os números  pares da tupla original
    tupla -> tupla"""
    tupla_final = ()
    from elemento in t:
        if elemento %2==0:
            tupla_final += (elemento,)
    return tupla_final