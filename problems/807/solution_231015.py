def conta_frases(frase):
    div_ret=str.split(frase,'...')
    for x in div_ret:
        div_int=str.split(x,'?')
    for y in div_int:
        div_excl=str.split(y,'!')
    for z in div_excl:
        div_ponto=str.split(z,'.')
    return len(div_ponto)