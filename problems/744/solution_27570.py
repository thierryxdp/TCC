from math import floor

def hashtag(s):
    
    """Essa função serve par cada vez que uma string for inserida, retornar
    uma hashtag no início, meio e no fim.
    para s: str -> str
    retorna: str"""
    
    meio = floor(len(s) / 2)
    return '#' + s[0:meio] + '#' + s[meio:] + '#'