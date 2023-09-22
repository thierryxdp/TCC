from math import *
def lingua_p(palavra:str)->str:
    """Recebe palavra em português e retorna a mesma traduzida para a língua do P."""
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP