def lingua_p(palavra):
    """retorna a palavra traduzida para lingua do P; str -> str"""
    a=str.lower(palavra)
    p='p'
    if 'a' in a:
        a=str.replace(a,'a','apa')
    if 'e' in a:
        a=str.replace(a,'e','epe')
    if 'i' in a:
        a=str.replace(a,'i','ipi')
    if 'o' in a:
        a=str.replace(a,'o','opo')
    if 'u' in a:
        a=str.replace(a,'u','upu')
    return a