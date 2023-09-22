def substitui (s,x,i):
    """Retorna uma string s onde o elemento i deve ser substituído por x"""

    pre = s[0:-i]
    pos = s[i+1len(s)]
    s = pre + x + pos
    return s