def uppCons(frase):
    ''' str -> str '''
    i = 0
    resposta = ""
    while i < len(frase):
        if str.upper(frase[i]) not in "AEIOU":
            resposta = resposta + str.upper(frase[i])
            i = i+1
        else:
            if str.upper(frase[i]) in "AEIOU":
                resposta = resposta + frase[i]
    return resposta