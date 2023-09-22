def freq_palavras(frases):
    dicionario = {}
    i = 0
    frases = str.replace(frases, ",","")
    frases = str.replace(frases, ".","")
    frases = str.lower(frases)
    frase = str.split(frases,)
    while i < len(frase):
        a = str.count(frases, frase[i])
        n = len(frase) - a
        dicionario[frase[i]] = str(n)
        i = i + 1
    return dicionario