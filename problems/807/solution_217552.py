def conta_frases(txt):
    argumentos=('...','.','!','?')
    frase=str.split(txt,argumentos)
    NF= len(frase)
    return NF