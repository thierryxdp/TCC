def lingua_p(palavra):
    """retorna a palavra traduzida para lingua do P; str -> str"""
    a=str.lower(palavra)
    p='p'
    v='aeiou'
    for x in a:
        if x in v:
            str.replace(a,x,x+p+x,1)
    return a