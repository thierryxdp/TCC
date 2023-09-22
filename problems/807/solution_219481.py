import re
def conta_frases(texto):
    """ Retorna o numero de frases em um texto;
    string->int """
    if "..." in texto:
        texto=texto.replace("...","?")
    return len(re.split("[.!?]",texto))-1