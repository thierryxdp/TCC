def conta_frases(frase):
    '''Função que conte o número de frase que aparecem no texto e retorne a frase sem os pontuações.
       str ---> int'''
    ponto_fi = str.count(frase,'.')
    ponto_excl = str.count(frase,'!')
    ponto_int = str.count(frase,'?')
    pontos_ret = str.count(frase,'...')
    sinal = ponto_excl + ponto_int + (ponto_fi - pontos_ret * 3) + pontos_ret
    return sinal