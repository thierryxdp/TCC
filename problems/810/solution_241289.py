def inverte(frase):
    '''Recebe uma frase e retorna outra com as mesmas palavras em ordem inversa, sem maisculos e sem pontuacao
    string -> string'''
    frase=str.lower(frase)
    frase=frase.replace(',','.')
    frase=frase.replace(':','.')
    frase=frase.replace(';','.')
    frase=frase.replace('!','.')
    frase=frase.replace('?','.')
    frase=frase.replace('.',' ')
    frase=frase.split(' ')
    fraseinv=frase[-1::-1]
    fraseinv=' '.join(fraseinv)
    fraseinv=fraseinv.strip()
    return fraseinv