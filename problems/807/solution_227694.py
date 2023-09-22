def conta_frases(frases):
    
    pontos = str.join('*', str.split(frases,'...'))
    
    tudo = str.count(pontos,'*') + str.count(pontos,'!') + str.count(pontos,'.')  + str.count(pontos,'?')


    
    return tudo