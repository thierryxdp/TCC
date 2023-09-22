def lingua_p(plvr):
    palavra = list (plvr)
    resultado = ''
    reposta = ''
    vogais = ' A E I O U a e i o u '
    for i in range (0, len(palavra)):
        
        if palavra[i] in vogais:
            resultado = palavra[i] +'p' + (palavra[i].lower())
        else:
            resultado = palavra[i] 
            
        resposta += resultado.lower()
    return resposta