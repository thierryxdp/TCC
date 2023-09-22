def freq_palavras(frases):
    dicionario = {}
    i = 0
    frase = str.split(frases,)
    while i < len(frase):
        a = str.strip(frases, frase[i])
        b = len(a)
        n = len(frase) - b
        dicionario = dicionario + dict.{frase[i]:n}
        i = i + 1
    return dicionario