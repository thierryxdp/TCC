def freq_palavras(frases):
    '''funçao dada uma string conta cada vez que um palavra aparece e coloca num dicionario
    str -> dic'''
    frase = str.split(frases)
    d = {}
    for i in frase:
        c = list.count(frase, i)
        d[i] = c
    return d