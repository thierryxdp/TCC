from math import *
def lingua_p(palavra):
    '''
    dada uma palavra em português, retorna a mesma palavra para língua do P.bRetorna a palvra na língua p. (str)
    '''
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP