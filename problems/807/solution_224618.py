def conta_frases(texto):
    """retorna o numero de frases que aparecem no texto; str -> int"""
    x=str.replace(texto,'...','.')
    a=str.split(x,'.')
    b=str.split(a[0],'!')+[str.split(a[1],'!')]+[str.split(a[2],'!')]+[str.split(a[3],'!')]+[str.split(a[4],'!')]+[str.split(a[5],'!')]
    c=str.split(b[0],'?')+[str.split(b[1],'?')]+[str.split(b[2],'?')]+[str.split(b[3],'?')]+[str.split(b[4],'?')]+[str.split(b[5],'?')]
    return len(c)