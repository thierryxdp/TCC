def uppCons(frase):
    vogais = 'aeiouúíóáéãõêâôîû'
    resposta = ''
    contador = 0
    letra= ' '
    while contador < len(frase)-1:
        if frase[contador] not in vogais:
            letra = frase[contador].upper()
        contador+=1
        resposta += letra
    return resposta