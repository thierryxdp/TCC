def lingua_p(s):
    """Função que converte uma palavra para a língua do p
    str -> str"""
    
    s_min = str.lower(s)
    t = ''
    for c in s_min:
        if c in 'aeiouéáú':
            t = t + c + 'p' + c
        else:
            t = t + c
    return t