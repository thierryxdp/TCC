def lingua_p(word):
    palavra = list(word)
    resultado = ''
    for i in range (0, len(palavra)):    
        if palavra[i] in 'aAeEiIoOuU':
            resultado = palavra[i] + 'p' + (palavra[i].lower())
        else:
            resultado = palavra[i]
        resposta = print (f'{resultado}', end='')
    return resposta