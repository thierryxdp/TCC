def conta_frases(x):
    '''
    Função que calcula o número de frases em uma string, sabendo que cada frase é terminada
    com um ponto final, um ponto de exclamação, um ponto de interrogação ou tres pontos em 
    sequencia(reticencias). É dado como entrada uma string.
    str->int 
    '''
    k=str.count(x,'...')
    b= str.count(str(str.split(x,'...')),'.')
    c=str.count(x,'!')
    v=str.count(x,'?')
    
    
    return (k+b+c+v)