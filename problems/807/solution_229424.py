def conta_frases(texto):
    '''
    
    '''
    reticencias = (3*'.')
    ponto_final = (1*'.')
    final = str.count((texto), ponto_final,0,len(texto))
    exclamacao = str.count((texto), '!',0,len(texto))
    interrogacao = str.count((texto), '?',0,len(texto))
    tres_pontos = str.count((texto), reticencias,0,len(texto))
    
    return final + exclamacao + interrogacao + tres_pontos