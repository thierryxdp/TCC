def substitui(s,x,i):
    '''Retorna uma string igual a s trocando a posicão i pelo caractere x.
    str,str,int-->str'''
    posi=i+1
    return s[ :i]+x+s[posi: ]