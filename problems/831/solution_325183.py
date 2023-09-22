def lingua_p(palavra):
    '''funcao que dado uma palavra
    retorn ela na lingua do p;str->str'''
    
    nova_palavra = ''
    for i in palavra:
        if i not in 'BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz':
            nova_palavra = nova_palavra + i + 'p' + i
        else:
            nova_palavra = nova_palavra + i
    return str.lower(nova_palavra)