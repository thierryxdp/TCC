def lingua_p(p):
    vogais = ['a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú']
    l = []
    for x in p:
        if x in vogais:
            l.append (x + "p" + x)
        else:
            l.append (x)
    return str.lower ("".join(l))