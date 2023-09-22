def lingua_p(palavra):
    """retorna a palavra traduzida para lingua do P; str -> str"""
    a=str.lower(palavra)
    p='p'
    v='aeiou'
    b=0
    while v[b] in a and b<len(v):
        str.replace(a,v[b],v[b]+p+v[b])
        b=b+1
    return a