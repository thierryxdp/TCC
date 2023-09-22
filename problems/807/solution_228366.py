def conta_frases(texto):
    """dada uma string em forma de texto retorna a quantidade de frases presentes
    str --> int"""
    frase_Repontuada=str.replace(texto,'!?...','.')
    return frase_Repontuada