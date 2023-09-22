def lingua_p(palavra):
    '''função que transofrma uma string palavra fornecida pelo usuário na língua do p.
    str -> str'''
    palavra_ = list(palavra)
    resultado = ''
    resposta = ''
    vogais = 'AEIOU aeiou À Á Â Ã É È Ê Í Î Ó Ô Õ Ú à á â ã é è ê ë í ó ò ô õ ú ù û ü'
    for i no intervalo (0, len(palavra_)):
        if palavra_[i] in vogais:
            resultado = palavra_[i] + 'p' + (palavra_[i].lower())

        else:
            resultado = palavra_[i]

            resposta = resposta + resultado.lower()

    return resposta