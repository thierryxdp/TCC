def substitui (s,x,i):
    """Retorna uma string s onde o elemento i deve ser substituído por x"""

    pre = s[0:-i]
    pos = s[-i:]
    i == x
    s = pre + pos
    return s