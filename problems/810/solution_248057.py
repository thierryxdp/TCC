def inverte(frase):
    '''
    
    '''
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_pontos = virgula.replace(':', ' ')
    ponto_virgula = dois_pontos.replace(';', ' ')
    ponto_final = ponto_virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    return ponto_exclamacao.join(reversed(list(text)))