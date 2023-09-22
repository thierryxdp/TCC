def lingua_p(word):
    '''função que transofrma uma string word, em português, fornecida pelo usuário na língua do p.
    str -> str'''
    palavra = list(word)
    resultado = ''
    resposta = ''
    vogais = 'AEIOU aeiou À Á Â Ã É È Ê Í Î Ó Ô Õ Ú à á â ã é è ê ë í ó ò ô õ ú ù û ü'
    for i in range(0, len(palavra)+1):
        if palavra[i] in vogais:
            resultado = palavra[i] + 'p' + (palavra[i].lower())

        else:
            resultado = palavra[i]

    resposta = resposta + resultado.lower()
    return resposta

    return resposta