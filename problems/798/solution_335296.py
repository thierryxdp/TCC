def freq_palavras(frases):
    lista = frases.split()
    dicio = {}
    for el in lista:
        dicio.update({el:lista.count(el)})
    return dicio