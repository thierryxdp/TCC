def conta_frases(txt):
    '''funcao que conta o numero de frases que aparecem em um texto, com suas restricoes. string -> int'''
    if txt.count("...")==1:
        return txt.count("!")+txt.count("?")+txt.count(".")-3
    elif txt.count<1:
        return texto.count("!")+txt.count("?")+txt.count(".")
    else:
        return txt.count("!")+txt.count("?")+txt.count(".")-6