def lingua_p(p):
    vogais = ['a','e','i','o','u', 'á', 'é', 'ú']
    l = []
    for x in p:
        if x in vogais:
            l.append(x + "p" + x)
        else:
            l.append(x)
    return str.lower("".join(l))