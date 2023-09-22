def conta_frases(frase):
    num_palavras=[n for n in frase if n=="!" or n=="?"]
    num_palavras2=tuple(num_palavras)
    frase1=str.split(frase,'...')
    frase2=frase1.split('.')
    
    return len(frase1)-1+len(num_palavras2)