def conta_frases(frases):
    pontos= str.join('*', str.split(frases,'...'))   
    return str.count(pontos,'*') + str.count(pontos,'!') + str.count(pontos,'.')  + str.count(pontos,'?')