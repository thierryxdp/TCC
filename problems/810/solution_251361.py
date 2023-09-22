def inverte(frase):
    ''' Retorna uma frase que contem as mesmas palavras da frase de entrada
        str -> str'''
    f=frase.split('!')
    f=' '.join(f)
    f=f.split('?')
    f=" ".join(f)
    f=f.split(',')
    f=" ".join(f)
    f=f.split('.')
    f=" ".join(f)
    f=f.split(';')
    f=" ".join(f)
    f=f.split(':')
    f=" ".join(f)
    f=f.split('-')
    f=" ".join(f)

    frase = f.lower()
    f = frase.split()
    f.reverse()
    frase_final = " ".join(f)


    return frase_final