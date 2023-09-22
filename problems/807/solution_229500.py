def conta_frases(x):
    '''
    str->int 
    '''
    tres_pontos=str.count(x,'...')
    ponto= str.count(str(str.split(x,'...')),'.')
    exclamacao=str.count(x,'!')
    interrogacao=str.count(x,'?')
    
    return (tres_pontos+ponto+exclamacao+interrogacao)