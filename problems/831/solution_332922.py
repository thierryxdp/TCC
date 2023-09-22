def lingua_p(p):
    np = str.lower(p)
    vogais = ['a', 'e', 'i', 'o', 'u']
    for i in vogais:
            np = str.replace(np, i, i + 'p' + i)
    return np