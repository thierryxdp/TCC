def quant_palavras(frase): #AULA 6
    """Retorne a quantidade de palavras dado uma frase;
    string - > int"""
    palavras = frase.split(" ")
    return len(palavras)

def conta_frases(texto):
    """Retorne a quantidade de frases dado um texto;
    string - > int"""
    texto = texto.replace("!",".").replace("?",".").replace("...",".")
    frases = texto.split(". ")
    return len(frases)