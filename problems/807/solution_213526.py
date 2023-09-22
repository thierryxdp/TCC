def conta_frases(frase):
    retorno=str.split(frase,'.')
    retorno=str.split(retorno,'!')
    retorno=str.split(retorno,'?')
    retorno=str.split(retorno,'...')
    return len(retorno)