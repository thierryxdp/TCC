def conta_frases(texto):
    '''
    
    '''
    
    
    exclamacao = str.count((texto), '!',0,len(texto))
    interrogacao = str.count((texto), '?',0,len(texto))
    tres_pontos = str.count((texto), '...',0,len(texto))
    
    return exclamacao + interrogacao + tres_pontos