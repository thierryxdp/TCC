def conta_frases(frase):
    num_palavras=[n for n in frase if n=="!" or n=="?"]
    num_palavras2=tuple(num_palavras)
    frase1=str.split(frase,'...')
    
    return len(frase1)