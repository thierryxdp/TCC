def conta_frases(frase):
    frase1=frase.split('...')
    f1=len(frase1)
    num_palavras=[n for n in frase1 if n== "!" or n== "?" or n== "."]
    num_palavras2=tuple(num_palavras)
    return frase1