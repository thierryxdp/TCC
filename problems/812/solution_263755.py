def retira_pontuacao(frase):
    
    '''
    Para retirarmos todos os pontos tivemos que criar uma peneira para cada pontuação,
    deva forma a frase ira passar por todas as peneiras e se necessario retirar os pontos.
    str > str> str
    '''
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    return e