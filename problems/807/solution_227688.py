def conta_frases(frases):
    
    pontos= str.join('-', str.split(frases,'...'))
        '''a = str.count(".",(frases))
    b = str.count("!",(frases))
    c = str.count("?",(frases))
    d = str.count("...",(frases))'''
    

    
    return str.count(pontos,'-') + str.count(pontos,'!') + str.count(pontos,'.')  + str.count(pontos,'?')