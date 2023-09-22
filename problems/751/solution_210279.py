def conta_frases(x):
    '''
    Função que calcula o número de frases em uma string, sabendo que cada frase é terminada
    com um ponto final, um ponto de exclamação, um ponto de interrogação ou tres pontos em 
    sequencia(reticencias). É dado como entrada uma string.
    str->int 
    '''
    tres_pontos= str.count(x,'...')
    ponto= str.count(str(str.split(x,'...')),'.')
    exclamacao=str.count(x,'!')
    interrogacao=str.count(x,'?')
    
    
    return (tres_pontos+ponto+exclamacao+interrogacao)