def posLetra (s, l, n):
    a = str.replace(s, l, 'k', n)
    b = str.replace(a, 'k', 'z', (n-1))
    return str.find(b, 'k')