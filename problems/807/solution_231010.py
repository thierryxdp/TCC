def conta_frases(frase):
    div_ret=str.split(frase,'...')
    div_int=str.split(div_ret[0]+div_ret[1],'?')
    div_excl=str.split(div_int[0]+div_int[1],'!')
    div_ponto=str.split(div_excl[0]+div_excl[1],'.')
    return len(div_ponto)