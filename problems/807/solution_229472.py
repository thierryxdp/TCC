def conta_frases(texto):
    '''
    
    '''
    final = str.count((texto), '.', 0, len(texto))
    exclamacao = str.count((texto), '!', 0, len(texto))
    interrogacao = str.count((texto), '?', 0, len(texto))
    tres_pontos = str.count(str(str.split(texto, '...')), '.', 0, len(texto))
    
    return (final + exclamacao + interrogacao + tres_pontos)