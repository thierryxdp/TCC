def Conta_frases(frase):
    '''Função que conte o número de frase que aparecem no texto e retorne a frase sem os pontuações.
       str ---> int'''
    ponto_fi = str.count(frase,'.')
    ponto_excl = str.count(frase,'!')
    ponto_int = str.count(frase,'?')
    pontos_ret = str.count(frase,'...')
    ponto_vir = str.count(frase,',')
    return (ponto_excl + ponto_int + ponto_vir + (ponto_fi - pontos_ret * 3) + pontos_ret)