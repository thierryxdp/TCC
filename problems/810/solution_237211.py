def inverte(frase):
    fras=frase.split()
    if '.' in fras: 
        fras.remove('.')
    if '!' in fras:
        fras.remove('!')
    if '?' in fras: 
        fras.remove('?')
    fras=''.join(fras)
    fras= fras[0].lower() + fras[1:]
    fras=fras.split(' ')
    fras.reverse()
    fras=' '.join(fras)
    return fras