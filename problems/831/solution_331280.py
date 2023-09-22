from math import *
def lingua_p(palavra):
    """dada uma palavra de entrada, retorna a palavra com
    a letra p inserida após cada vogal e toda em minísculas"""
    palavraMin=str.lower(palavra)
    letras=list(palavraMin)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP