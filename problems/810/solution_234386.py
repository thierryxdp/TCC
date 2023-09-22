def inverte(frase):
    frase_fatiada = str.split(frase)
    return frase_fatiada[-1:-(len(frase_fatiada)-1:-1]