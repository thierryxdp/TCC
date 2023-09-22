def lingua_p(palavra):
    '''Dado uma palavra, ira retornar a palavra na língua do P.
    str->str'''
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP