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
    if 'á' in a:
        a=str.replace(a,'á','ápá')
    if 'é' in a:
        a=str.replace(a,'é','épé')
    if 'í' in a:
        a=str.replace(a,'í','ípí')
    if 'ó' in a:
        a=str.replace(a,'ó','ópó')
    if 'ú' in a:
        a=str.replace(a,'ú','úpú')
    return a