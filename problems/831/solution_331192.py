def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna ela traduzida para a
    língua do P( P+vogal anterior)
    valor de entrada: str
    valor de saída: str'''
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP