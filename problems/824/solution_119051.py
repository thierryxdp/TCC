def cons(x):
    return x not in ("a", "e", "i", "o", "u", "ó", "ú","é","à","á","í", "ê", "ã", "â", "ô")
def uppCons(s):
    """Recebe todas as consoantes e retorna a frase com as consoantes maiusculas"""
    r = []
    for e in s:
        if cons(e):
            r.append(e.upper())
        else:
            r.append(e)
    return str.join("",r)