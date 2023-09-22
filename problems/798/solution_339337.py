def freq_palavras(frase):
    palavras = frase.split()
    dict = {}
    counter = 0 
    for elementos in palavras:
        dict[palavras[counter]] = palavras.count(palavras[counter])
        counter += 1
        return dict