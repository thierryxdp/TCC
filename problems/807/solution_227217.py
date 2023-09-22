def conta_frases(frase):
    """Funcao que dado um texto, o separa de acordo com '!','?' e "..."""
    w=frase.replace('...','.')
    x=w.replace('.','!')
    y=x.replace('?','!')
    z=y.split('!')
    bug=len(z)
    resposta=bug-1
    return resposta