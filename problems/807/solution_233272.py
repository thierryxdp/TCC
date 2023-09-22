def conta_frases(x):
    '''Conta o numero de frases presente numa string.
    A frase é  considerada acabada quando aparecem
    os sinas de pontuação: '.', '...', '!' e '?', logo,
    caso haja mais frases escritas
    elas aparecerão após os sinais.'''
    assinatura: str > int
    casos de teste:
    cont_ret = str.count(x,'...')

    t= str.replace(x,'...','')
    cont_pont = str.count(t,'.')
    
    cont_inte = str.count(x,'?')

    cont_ex = str.count(x,'!')

    return cont_ret + cont_pont + cont_inte + cont_ex