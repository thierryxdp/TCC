def lingua_p(word):
    palavra = list(word)
    resultado = ''
    resposta = ''
    for i in range (0, len(palavra)):
        
        if palavra[i] in 'aAeEiIoOuU':
            resultado = palavra[i] + 'p' + (palavra[i].lower())

        else:
            resultado = palavra[i]

        resposta += resultado.lower()

    return resposta