def conta_frases(frases):
    """função que dado um texto, retorne o número de frases que o texto possui; string -->int"""
    frases= frases.replace("!",".")
    frases= frases.replace("?",".")
    frases= frases.replace("...",".")
    frases= frases.split(".")
    frases= frases.split(" ")
    return len(frases)