def inverte(frase):
    '''Recebe uma frase e retorna uma frase com as mesmas palavras na ordem inversa sem letras maiusculas
    e sem pontuacao.
    str -> str'''
    frase=str.lower(frase)
    frase=frase.replace(',','.')
    frase=frase.replace(':','.')
    frase=frase.replace(';','.')
    frase=frase.replace('!','.')
    frase=frase.replace('?','.')
    frase=frase.split('.')
    fraseinv=frase[-1::-1]
    fraseinv=' '.join(fraseinv)
    fraseinv=fraseinv.strip()
    return fraseinv