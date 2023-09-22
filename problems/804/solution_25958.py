def filtra_pares(t):
    """função que retorna somente os números  pares da tupla original
    tupla -> tupla"""
    tupla_final = ()
    n = 0
    while n<len(t):
        if t[n]%2==0:
            tupla_final += (t[n],)
        n +=1
    return tupla_final