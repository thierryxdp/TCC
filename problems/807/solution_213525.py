def conta_frases(frase):
    retorno=str.split(frase,'.')
    retorno=str.split(retorno,'!')
    retorno=str.split(frase,'?')
    retorno=str.split(frase,'...')
    return len(retorno)