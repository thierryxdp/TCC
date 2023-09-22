def lingua_p(palavra):
    '''Dado uma palavra, retorna está palavra para língua do P. strin-->string.'''
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP