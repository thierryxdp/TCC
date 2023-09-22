def lingua_p(word):
    palavra = list(word)
    resultado = ''
    resposta = ''
    vogais = 'A E I O U a e i o u À Á Â Ã É È Ê Í Ì Î Ó Ò Ô Õ Ú Ù Û à á â ç é è ê í ì î ó ò ô õ ú ù û'
    for i in range (0, len(palavra)):
        
        if palavra[i] in vogais:
            resultado = palavra[i] + 'p' + (palavra[i].lower())

        else:
            resultado = palavra[i]

        resposta += resultado.lower()

    return resposta