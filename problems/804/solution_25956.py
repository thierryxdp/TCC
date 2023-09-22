def filtra_pares(t):
    """função que retorna somente os números  pares da tupla original
    tupla -> tupla"""
    tupla_final = ()
    from elem in t:
        if elem%2==0:
            tupla_final += (elem,)
        return tupla_final