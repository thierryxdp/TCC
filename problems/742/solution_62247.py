def substitui(s, x, i):
    '''Retorna a string igual a str, exceto que o elemento da posição i vai ser substituido pelo caractere x'''
    '''str,str,int --> str'''
    str1[i] = x
    
    return str1[0:i] + x + str1[i:-1]