def conta_frases(frase):
    '''Um função que conta as frases de uma string recebida como entrada str => int'''
    ponto = frase.count(".")
    excla = frase.count("!")
    inter = frase.count("?")
    reti = frase.count("...")
    if reti == 1:
        return (ponto-1*3) + excla + inter + reti
    elif reti == 2:
        return (ponto-2*3) + excla + inter + reti
    else:
        return ponto + excla + inter + reti