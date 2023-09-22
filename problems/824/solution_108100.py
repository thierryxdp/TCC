def uppCons(frase):
    i = 0
    resposta = ''
    
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            resposta = resposta + frase[i]
        else:
            resposta = resposta + str.upper(frase[i])
        i = i+1