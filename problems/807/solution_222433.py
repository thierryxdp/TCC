def conta_frases(texto):
    #Função que conta quantas frases há em um texto
    #str -> int
    total = texto.count(".")+texto.count("!")+texto.count("?")+texto.count("...")-(3*texto.count("..."))
    return total