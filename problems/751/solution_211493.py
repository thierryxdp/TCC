def conta_frases(x):
    ''' string > int
    Conta o numero de frases presente numa string. A frase é dada como terminada quando aparecem
    os seguintes sinais de pontuação: '.', '...', '!' e '?', logo, caso haja mais frases escritas
    elas aparecerão após os sinais.'''
    
    cont_ret = str.count(x,'...')

    t= str.replace(x,'...','')
    cont_pt = str.count(t,'.')
    
    cont_interroga = str.count(x,'?')

    cont_exclama = str.count(x,'!')

    return cont_ret + cont_pt + cont_interroga + cont_exclama