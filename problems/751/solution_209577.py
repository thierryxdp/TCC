def quant_palavras(frase):
    """Esta função calcula quantas palavras há em uma frase.
    str->int"""
    if ' ' not in frase[0] and ' ' not in frase[len(frase)-1]:
        numero_palavras1=str.count(frase,' ')+ 1
        return numero_palavras1
    elif (' ' in frase[0] and ' ' not in  frase[len(frase)-1]) or (' ' not in x[0] and ' ' in x[len(x)-1]):
        numero_palavras2=str.count(frase,' ')
        return numero_palavras2
    else:
        numero_palavras3=str.count(frase,' ')-1
        return numero_palavras3