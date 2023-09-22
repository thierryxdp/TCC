def conta_frases(texto):
    """dada uma string em forma de texto retorna a quantidade de frases presentes
    str --> int"""
    frase_Repontuada=str.replace(texto,'!','.')
    frase_Repontuada=str.replace(frase_Repontuada,'?','.')
    frase_Repontuada=str.replace(frase_Repontuada,'...','.')
    return len(str.split(frase_Repontuada,'.'))