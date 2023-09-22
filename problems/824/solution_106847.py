def uppCons(frase):
    vogais = 'aeiouúíóáéãõêâôîû'
    resposta = ''
    contador = 0
    letra= ' '
    while contador < len(frase):
        if frase[contador] not in vogais:
            letra = frase[contador].upper()
        else:
            letra = frase[contador]
        contador+=1
        resposta += letra
    return resposta