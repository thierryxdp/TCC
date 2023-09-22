def conta_frases(texto):
    numero=texto.count('...')*(-2)
    numero+=texto.count('!')
    numero+=texto.count('?')
    numero+=texto.count('.')
    if numero == 0:
        numero+= 1
        return numero
    else:
        return numero