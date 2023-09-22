def inverte(frase):
    'Funcao que dada uma frase, retorne a mesma de maneira invertida'
    'str -> str'
    frase = frase.replace('—',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = frase.lower()
    frase = frase.split()
    frase = list(reversed(frase))
    return (' '.join(frase))
 return frase