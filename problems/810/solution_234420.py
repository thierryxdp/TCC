def inverte(frase):
    """Esta função retira todos os caracteres de pontuação no texto, e
       inverte a ordem das palavras"""
    
    frase = str.lower(frase)
    pontuacao = '!','?','.',',','-'
    for car in pontuacao:
        frase = frase.replace(car, '')
    
    x = str.split(frase,' ')
    y = x[-1::-1]
    z = str.join (' ',y)
    w = str.lower(z)
    return w