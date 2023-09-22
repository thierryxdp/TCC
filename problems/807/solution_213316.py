def conta_frases(txt):
    '''funcao que conta o numero de frases que aparecem em um texto, com suas restricoes. string -> int'''
    if texto.count("...")==1:
        return texto.count("!")+texto.count("?")+texto.count(".")-3
    elif texto.count<1:
        return texto.count("!")+texto.count("?")+texto.count(".")
    else:
        return texto.count("!")+texto.count("?")+texto.count(".")-6