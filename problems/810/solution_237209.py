def inverte(frase):
    frase=frase.split('')
    if '.' in frase: 
        frase.remove('.')
    if '!' in frase:
        frase.remove('!')
    if '?' in frase: 
        frase.remove('?')
    fras=''.join(frase)
    fras= fras[0].lower() + fras[1:]
    fras=fras.split(' ')
    fras.reverse()
    fras=' '.join(fras)
    return fras