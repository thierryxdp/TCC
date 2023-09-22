def muda(frase):
    fras=substitui(frase)
    fras= fras[0].lower() + fras[1:]
    fras=fras.split(' ')
    fras.reverse()
    fras=' '.join(fras)
    return fras