def lingua_p (word):
    palavra = list(word)
    resutado = " "
    resposta = " "
    vogais = 'A E I O U a e i o u á é í ó ú Á É Í Ó Ú â ê ô õ ã Â Ê Ô Ã Õ Á á'
    for i in range (0, len(palavra)):
        if palavra [i] in vogais:
            resultado = palavra[i] + 'p' + (palavra[i].lower())
        else:
            resultado = palavra [i]
            
        resposta += resutado.lower()
    return resposta