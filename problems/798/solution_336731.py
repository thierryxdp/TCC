def freq_palavras(frase):
    chaves = frase.split()
    valores = []
    for i in range(len(chaves)):
        palavra = chaves[i]
        valores.append(chaves.count(palavra))
    return dict(zip(chaves,valores))