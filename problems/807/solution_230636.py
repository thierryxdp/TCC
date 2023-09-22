def conta_frases(x):
    ''' string > int
    Conta o numero de frases presente numa string. A frase é dada como terminada quando aparecem
    os seguintes sinais de pontuação: '.', '...', '!' e '?', logo, caso haja mais frases escritas
    elas aparecerão após os sinais.'''
    
    for i in x:
        return str.count(x,'.') + str.count(x,'...') + str.count(x,'!') + str.count(x,'?')