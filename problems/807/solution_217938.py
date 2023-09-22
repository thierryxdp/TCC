def conta_frases(frase):
    num_palavras=[n for n in frase if n=="!" or n=="?"]
    num_palavras2=tuple(num_palavras)
    return len(num_palavras2)