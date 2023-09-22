def lingua_p(palavra):
    '''retorna a palavra intercalada com letra p.'''
    '''str=>str'''
    p=''
    for letra in palavra:
        p+=letra
        if letra in 'aáãàâeèéêiíìoòóôõuúù':
        p += 'p' +letra
    return p