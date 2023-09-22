def hashtag(s):
    """Dada uma string retorna a mesma com o caracter # no início, final e meio.
    str -> str"""
    
    metade = int(len(s)/2)
    
    return '#' + s[:metade] + '#' + s[0 + metade:] + '#'