def lingua_p(palavra):
    '''funcao que dado uma palavra
    retorn ela na lingua do p;str->str'''
    nova_palavra = ''
    for i in len(palavra):
        if palavra[i] not in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            nova_palavra = nova_palavra + str.replace(palavra,str.lower(palavra[i]),palavra[i]+'p')
    return nova_palavra