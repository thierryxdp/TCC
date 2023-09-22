def inverte(frase):
    """Esta função retira todos os caracteres de pontuação no texto, e
       inverte a ordem das palavras"""
    pontuacao = "!","?",".",",","-"
    for car in pontuacao:
        frase = frase.replace(car, " ")
    
    x = frase.split (" ")
    y = x[-1::-1]
    z = str.join (" ",y)
    w = str.lower(z)
    print  y = x[-1::-1]