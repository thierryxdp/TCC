def conta_frases(texto):
    lista = []
    for v in texto:
        if v.isupper():
            lista += [v]
    return len(lista)