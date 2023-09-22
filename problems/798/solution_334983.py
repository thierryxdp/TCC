def freq_palavras(frases):
    dicionario = {}
    i = 0
    frases = str.replace(frases, ",","")
    frases = str.replace(frases, ".","")
    frase = str.split(frases,)
    while i < len(frase):
        a = list.count(frase, frase[i])
        dicionario[frase[i]] = str(a)
        i = i + 1
    return dicionario