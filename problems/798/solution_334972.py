def freq_palavras(frases):
    dicionario = {}
    i = 0
    frases = str.replace(frases, ",","")
    frases = str.replace(frases, ".","")
    frases = str.lower(frases)
    frase = str.split(frases,)
    while i < len(frase):
        while i < len(frase):
            a = list.remove(frase, frase[i])
        b = len(a)
        n = len(frase) - b
        dicionario[frase[i]] = str(n)
        i = i + 1
    return a