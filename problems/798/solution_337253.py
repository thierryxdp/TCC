def freq_palavras(frases):
    separar = frases.split()
    dicio = {}

    for palavra in separar:
        if palavra in dicio:
            dicio[palavra] += 1
        else:
            dicio[palavra] = 1

    for key in list(dicio.keys()):
        print(key, ':', dicio[key])