def uppCons(frase):
    i = 0
    resposta = ' '
    
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            resposta = resposta + str(frase[i])
        else:
            resposta = resposta + str(str.upper(frase[i]))
        i = i+1