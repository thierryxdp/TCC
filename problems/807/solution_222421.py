def conta_frases(texto):
    #Função que conta quantas frases há em um texto
    #str -> int
    new_texto = texto.strip('...')
    total = new_texto.count(".")+new_texto.count("!")+new_texto.count("?")
    return total+texto.count("...")