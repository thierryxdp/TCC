def substitui(s,x,i):
    '''retorna uma string ihual a s, e o elemento da posição i é substituído pelo caractere x'''
    '''str, int, int -> str'''
    s[i]=x
    return s
    return s [0:i] + x + s [i + 1:]