def inverte(frase):
    """Esta função retira todos os caracteres de pontuação no texto, e
       inverte a ordem das palavras"""
    pontuacao = "!","?",".",",","-"
    for car in pontuacao:
        frase = frase.replace(car, " ")
    
    x = frase.split (" ")
    y = x[::-1]
    v = y[1::-1]
    z = str.join (" ",v)
    w = str.lower(z)
    return  w