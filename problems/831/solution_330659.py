def lingua_p (frase):
    frase = frase.lower()
    lista = list(frase)
    i = 0
    frase2 = ""
    for l in lista :
        if l in "aeiou":
            lista.insert(i+1, "p"+l)
            i += + 1
        else:
            i += +1
    frase2 = frase2.join(lista)
    return frase2