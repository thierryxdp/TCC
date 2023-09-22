def lingua_p(p):
    np = str.lower(p)
    vogais = ['a','ã', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']
    for i in vogais:
            np = str.replace(np, i, i + 'p' + i)
    return np