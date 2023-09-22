def lingua_p(palavra):
    '''
    string --- > string
    '''
    palavra = palavra.lower()
    palavra_p = ''
    for i in palavra:
        if i in 'áaeéiíoóuúAÁEÉIÍOÓUÚ':
            palavra_p += i+'p'+i
        else:
            palavra_p += i
    return palavra_p