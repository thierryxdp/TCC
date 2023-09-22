def conta_frases(frase):
    num_palavras=[n for n in frase if n =="!" and n=="."]
    num_palavras2=tuple(num_palavras)
    return num_palavras2