def conta_frases(texto):
    '''Conta quantas frases aparecem no texto
    str->int'''
    split1=str.split(texto,'...')
    split2=str.split(split1,'!')
    split3=str.split(split2,'?')
    split4=str.split(split3,'.')
    return len(split4)