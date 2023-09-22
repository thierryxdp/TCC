def substitui(s,x,i):
    '''str, str, int -> string'''
    '''esta função retorna uma string s, exceto o elemento da posição i, que é substituído por 'x' '''
    return s[0:i] + x + s[i + 1:]