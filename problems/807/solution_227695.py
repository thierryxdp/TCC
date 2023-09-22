def conta_frases(frases):
    
    pontos = str.join('*', str.split(frases,'...'))
    
    tudo = str.count(pontos,'*') + str.count(pontos,'!') + str.count(pontos,'.')  + str.count(pontos,'?')

    '''
    para efetuar essa contagem tivemos que alterar a informação dos '...',
    pois na hora da contagem estaria sendo confundido com o '.',
    depois tivemos que contabilicar todos os sinal (. - ! - ? - ...(*))
    str > str > int
    '''
    
    return tudo