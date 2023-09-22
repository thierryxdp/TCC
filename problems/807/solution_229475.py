def conta_frases(c):
    '''
    Função que calcula o número de frases em uma string, sabendo que cada frase é
    terminada com um ponto final, um ponto de exclamação, um ponto de interrogação
    ou tres pontos em sequencia(reticencias).
    str->int 
    '''
    tres_pontos=str.count(c,'...')
    ponto= str.count(str(str.split(c,'...')),'.')
    exclamacao=str.count(c,'!')
    interrogacao=str.count(c,'?')
    
    
    return (tres_pontos+ponto+exclamacao+interrogacao)