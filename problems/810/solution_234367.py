def inverte(frase):
    """Esta função retira todos os caracteres de pontuação no texto, e
       inverte a ordem das palavras"""
    pontuacao = "!","?",".",",","-"
    for car in pontuacao:
        frase = frase.replace(car, " ")
    
    x = frase[1::-1]
    y = x.split (" ")
    z = str.join (" ",y)
    w = str.lower(z)
    return  w