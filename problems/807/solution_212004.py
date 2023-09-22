def conta_frases(frase):
    """retorna o numero de frases
    str->float"""
    s=str.split(frase,'!')
    v=str.split(frase,'.')
    y=str.split(frase,'?')
    u=str.split(frase,'...')
    t=len((str.split(frase,'!'))+(str.split(frase,'.'))+(str.split(frase,'?'))+(str.split(frase,'...')))
    return t