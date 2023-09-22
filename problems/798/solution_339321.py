def freq_palavras(frase):
    palavras = frase.split()
    dict1 = {}
    counter = 0
    str-->dict
    
    for elementos in palavras:
        dict1[palavras[counter]] = palavras.count(palavras[counter])
        counter += 1
        return dict1