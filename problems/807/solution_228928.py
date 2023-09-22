def conta_frases(numFrases):
    '''
    funcao utilizada para contar o numero de frases
    pontos de interrogacao e exclamacao não aparecerao em
    sequencia
    str->int
    '''
    a= str.join('.', str.split(numFrases, '...'))
    c= str.join('.', str.split(a, '?'))
    d= str.join('.', str.split(c, '!'))
    solucao=str.count( d, '.')
    return solucao