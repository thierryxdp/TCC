def inverte(frase):
    ''' Essa função inverte a frase, retirando toda pontuação e adicionando um espaço no local,
    depois retorna um a frase com as alterações'''
    if ':' in frase:
        frase= frase.replace(':',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if '.' in frase:
        frase= frase.replace('.',' ')
    if '!' in frase:
        frase= frase.replace('!',' ')
    if '?' in frase:
        frase= frase.replace('?',' ')
    if '-' in frase:
        frase= frase.replace('-',' ')
    if ';' in frase:
        frase= frase.replace(';',' ')
    frase= str.reverse(frase)
    return frase