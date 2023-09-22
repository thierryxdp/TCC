def inverte(frase):
    """funçãp que recebe uma frase e retorna essa mesma frase
    na ordem inversa com as mesmas palavras.
    str -> <frase>"""
    frase  = frase.replace('?','')
    frase  = frase.replace('!','')
    frase  = frase.replace(',','')
    frase  = frase.replace('-',' ')
    frase  = frase.replace(':',' ')
    frase  = frase.replace(';',' ')
    frase  = frase.replace('.','')
    frase  = frase.split(' ')
    frase  = frase[-1::-1]
    frase  = str.strip(str.lower(str.join(' ', frase)))

    return frase