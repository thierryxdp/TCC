#vai criar um dicionario com a palavra e a quant de vezes que ela aparece
# frase .split vai dividir a str e retornar listas
def freq_palavras(frases):
    r = dict()
    for frase in frases.split():
        if frase in r:
            r[frase] += 1
        else:
            r[frase] = 1
    return r