def conta_frases(texto):
    '''Função que conta o número de frases que aparecem no texto, cada frase no texto  ́e terminada com um ponto final, um ponto de exclamação, um ponto
de interrogação ou três pontos em sequência; str-> int '''
    texto.replace('?', '.')
    texto = texto.replace('?', '.')
    texto.replace('!', '.')
    texto=texto.replace('!', '.')
    texto.replace('...', '.')
    texto = texto.replace('...', '.')
    texto.split ('.')
    texto= texto.split ('.')
    
    return len(texto)-1