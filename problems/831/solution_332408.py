def lingua_p(palavra):
    """Função que receba como parâmetro uma palavra
    (em português) e retorne esta mesma palavra traduzida
    para a língua do P. Uma palavra foi traduzida para a
    língua do P quando, após cada vogal da palavra original,
    é inserida a sequência de letras 'p' mais a vogal original.
    str -> str"""
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP