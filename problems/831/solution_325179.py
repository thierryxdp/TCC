def lingua_p(palavra):
    '''funcao que dado uma palavra
    retorn ela na lingua do p;str->str'''
    
    for i in len(palavra):
        if palavra[i] not in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            str.replace(palavra,str.lower(palavra[i]),palavra[i]+'p')
    return palavra