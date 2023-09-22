def conta_frases(frases):
    """ retorna o numero de frases dado um texto, str->int"""
    frases1=frases.replace("...",".")
    frases2=frases1.replace("!",".")
    frases3=frases2.replace("?",".")
    return len(frases3.split("."))-1