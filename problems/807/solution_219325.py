import re
def conta_frases(texto):
    """ Retorna o numero de frases em um texto;
    string->int """
    return len(re.split("[.!?...]",texto))-1