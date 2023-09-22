def inverte(frase):
    ''' Essa função inverte a frase, retirando toda pontuação e adicionando um espaço no local,
    depois retorna um a frase com as alterações'''
    list.reverse(frase)
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
    return frase