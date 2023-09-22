def substitui(s, x, i):
    '''Retorna a string igual a str, exceto que o elemento da posição i vai ser substituido pelo caractere x'''
    '''str,str,int --> str'''
    
    return s[0:i] + x + s[0:-1:i]