def conta_frases(texto):
    #Função que conta quantas frases há em um texto
    #str -> int
    if str.count(texto, "...")>0:
        strip = str.strip(texto, "...")
        total = strip.count(".")+strip.count("!")+strip.count("?")
        return total + texto.count("...")
    else:
        total = texto.count(".")+texto.count("!")+texto.count("?")
        return total