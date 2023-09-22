substitui(str, x, i):
    '''Retorna a string igual a str, exceto que o elemento da posição i vai ser substituido pelo caractere x'''
    '''str,str,int --> str'''
    return str[0:i] + x + str[i:-1]