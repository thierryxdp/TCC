def lingua_p(s):
    """Função que converte uma palavra para a língua do p
    str -> str"""
    
    r = str.lower(s)
    t = ''
    for c in r:
        if c in 'aeiou':
            t = t + 'p' + c
    return t