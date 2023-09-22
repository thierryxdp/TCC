def uppCons(frase):
    '''transforma todas as consuantes da string de entrada em maiúsculas;
    str -> str'''
    nova_frase = ''
    for i in frase:
        if i in 'bcdffghjklmnpqrstvwxyz':
            nova_frase += str(i).upper()
        else:
            nova_frase += str(i)
    return nova_frase