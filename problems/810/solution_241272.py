def aaa(frase):
    frase=frase.replace(',','.')
    frase=frase.replace(':','.')
    frase=frase.replace(';','.')
    frase=frase.replace('!','.')
    frase=frase.replace('?','.')
    frase=frase.replace('.',' ')
    frase=frase.split(' ')
    frase=frase[-1::-1]
    fraseinv=' '.join(frase)
    fraseinv=fraseinv.strip()
    return fraseinvdef